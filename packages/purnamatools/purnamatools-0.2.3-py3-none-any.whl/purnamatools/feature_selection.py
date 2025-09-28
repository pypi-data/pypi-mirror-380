import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LassoCV, Lasso
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.ensemble import  RandomForestRegressor
from sklearn.feature_selection import mutual_info_classif, mutual_info_regression



def correlation_analysis(df, target, method='pearson', threshold=0.4, top_n=20):
    """
    Perform correlation analysis with target and multicollinearity check.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe containing features + target
    target : str
        Target column name (must be numeric)
    method : str, default='pearson'
        Correlation method ('pearson', 'spearman', 'kendall')
    threshold : float, default=0.4
        Threshold to determine strong correlation with target
    top_n : int, default=20
        Show top N features by correlation strength
    
    Returns
    -------
    dict
        Dictionary with keys:
        - "strong_corr": Strong correlations with target
        - "correlated_groups": Groups of features that are highly correlated with each other
        - "drop_cols": Features suggested to drop (keeping one feature per group)
    """
    
    # --- 0. Keep only numeric columns ---
    df_num = df.select_dtypes(include=[np.number]).dropna()
    if target not in df_num.columns:
        raise ValueError(f"Target '{target}' not found or not numeric.")
    
    corr_matrix = df_num.corr(method=method)
    
    # --- 1. Heatmap of full correlation matrix ---
    plt.figure(figsize=(12, 8))
    sns.heatmap(corr_matrix, cmap="coolwarm", center=0, annot=False)
    plt.title(f"Full Correlation Matrix ({method})")
    plt.show()
    
    # --- 2. Correlation with target ---
    corr_target = corr_matrix[target].drop(target).sort_values(key=lambda x: x.abs(), ascending=False)
    
    # Barplot top_n
    plt.figure(figsize=(8, 6))
    sns.barplot(
        x=corr_target.head(top_n).values,
        y=corr_target.head(top_n).index,
        palette="coolwarm"
    )
    plt.axvline(x=threshold, color='green', linestyle='--', label=f"Threshold {threshold}")
    plt.axvline(x=-threshold, color='green', linestyle='--')
    plt.title(f"Top {top_n} Correlations with {target}")
    plt.legend()
    plt.show()
    
    # --- 3. Strong correlations ---
    strong_corr = corr_target[abs(corr_target) >= threshold]
    if not strong_corr.empty:
        print("\n📌 Strong correlations with target:")
        display(strong_corr.to_frame(name="Correlation"))
    else:
        print(f"\n⚠️ No strong correlations with {target} (>|{threshold}|).")
    
    # --- 4. Multicollinearity / Correlated feature groups ---
    corr_features = corr_matrix.drop(target, axis=0).drop(target, axis=1)
    redundant = []

    # Cari semua pasangan fitur yang tinggi korelasinya (>0.9)
    for col in corr_features.columns:
        for row in corr_features.index:
            if col < row and abs(corr_features.loc[row, col]) > 0.9:
                redundant.append((row, col, corr_features.loc[row, col]))

    redundant_df = pd.DataFrame(redundant, columns=["Feature 1", "Feature 2", "Correlation"])
    
    if not redundant_df.empty:
        print("\n⚠️ Potential redundant features detected (|correlation| > 0.9):")
        display(redundant_df.sort_values("Correlation", ascending=False))
        
        # --- Kelompokkan fitur yang saling berkorelasi menjadi grup ---
        groups = []
        for f1, f2, _ in redundant:
            added = False
            for g in groups:
                if f1 in g or f2 in g:
                    g.update([f1, f2])
                    added = True
                    break
            if not added:
                groups.append(set([f1, f2]))
        
        # Tampilkan setiap group
        group_list = [list(g) for g in groups]
        print("\n📌 Correlated Groups:")
        for i, g in enumerate(group_list, 1):
            print(f"Group {i}: {g}")
        
        # --- Pilih 1 fitur terbaik per grup berdasarkan korelasi ke target ---
        drop_cols = []
        for g in groups:
            best = max(g, key=lambda x: abs(corr_target.get(x, 0)))
            drop_cols.extend(g - set([best]))
        
        print("\n💡 Features to drop (others in the group):")
        display(drop_cols)
    
    else:
        print("\n✅ No highly redundant features found.")
        group_list = []
        drop_cols = []
    
    # --- Return hasil ---
    return {
        "strong_corr": strong_corr,
        "correlated_groups": group_list,
        "drop_cols": drop_cols
    }
    
def mi_analysis(df, target, problem="regression", top_n=20, random_state=42):
    """
    Mutual Information (MI) feature selection.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe containing features + target
    target : str
        Target column name (must be numeric for regression, can be categorical for classification)
    problem : str
        'regression' or 'classification'
    top_n : int
        Show top N features by MI score
    random_state : int
        Random seed for reproducibility

    Returns
    -------
    Dictionary with keys:
        - "mi_df" : pd.DataFrame Sorted dataframe of features and their MI scores
        - "best_features" : list List of top N features by MI score
    """

    # Pisahkan X dan y
    df_num = df.select_dtypes(include=[np.number]).dropna()
    if target not in df_num.columns:
        raise ValueError(f"Target '{target}' not found or not numeric.")
    
    X = df_num.drop(columns=[target])
    y = df_num[target]

    # Pilih fungsi MI sesuai problem
    if problem == "regression":
        mi = mutual_info_regression(X, y, random_state=random_state)
    elif problem == "classification":
        mi = mutual_info_classif(X, y, random_state=random_state)
    else:
        raise ValueError("Problem must be 'regression' or 'classification'.")

    # Buat DataFrame hasil
    mi_df = pd.DataFrame({
        "feature": X.columns,
        "mi_score": mi
    }).sort_values("mi_score", ascending=False).reset_index(drop=True)

    # --- Plot bar chart top_n ---
    plt.figure(figsize=(8, 6))
    sns.barplot(x="mi_score", y="feature", data=mi_df.head(top_n), palette="viridis")
    plt.title(f"Top {top_n} Features by Mutual Information ({problem})")
    plt.xlabel("MI Score")
    plt.ylabel("Feature")
    plt.show()

    # --- Print & display ---
    print("\n📌 Top features by MI Score:")
    display(mi_df.head(top_n))

    # Ambil list top features
    best_features = mi_df.head(top_n)["feature"].tolist();

    return {
        "mi_df": mi_df,
        "best_features": best_features
    }

def batch_rfe(X, y, 
                                base_estimator=None, 
                                n_features_to_select=2, 
                                batch_size=None, 
                                final_top=10):
    """
    Scalable Recursive Feature Elimination (RFE) with optional batch mode.

    This function performs RFE for feature selection, with support for batching
    when the number of features is very large. Features are optionally processed
    in batches, and the best from each batch are combined for a final RFE.

    Parameters
    ----------
    X : pd.DataFrame
        Feature matrix.
    y : pd.Series or np.ndarray
        Target variable.
    base_estimator : sklearn estimator, optional
        Model used to evaluate features. If None, defaults to:
        - RandomForestClassifier(random_state=42, n_jobs=-1)
    n_features_to_select : int, default=2
        Number of top features to select in each batch.
    batch_size : int or None, default=None
        Number of features per batch. If None, standard RFE is run on all features.
    final_top : int, default=10
        Number of features to select in the final RFE stage
        (only applies if batching is used).

    Returns
    -------
    tuple
        selected_features : list of str
            List of features selected by the final RFE stage.
        ranking_df : pd.DataFrame
            DataFrame containing all features from the final stage with their
            ranking (1 = selected, higher = eliminated earlier).

    Notes
    -----
    - If batch_size is None, standard RFE is applied to all features.
    - In batch mode, features are first reduced per batch, then combined
    for a final RFE to produce the final selection.
    """
    if base_estimator is None:
        from sklearn.ensemble import RandomForestClassifier
        base_estimator = RandomForestClassifier(random_state=42, n_jobs=-1)
    
    from sklearn.feature_selection import RFE

    feature_names = X.columns.tolist()
    
    # === Case 1: Standard RFE (no batching) ===
    if batch_size is None:
        rfe = RFE(base_estimator, n_features_to_select=final_top)
        rfe.fit(X, y)
        final_selected = [f for f, s in zip(feature_names, rfe.support_) if s]
        ranking_df = pd.DataFrame({
            "Feature": feature_names,
            "Ranking": rfe.ranking_
        }).sort_values("Ranking")
        print("\n=== Final Selected Features (No Batch) ===")
        print(final_selected)
        display(ranking_df)
        return final_selected, ranking_df
    
    # === Case 2: Batched RFE ===
    selected_features = []
    n_features = len(feature_names)

    # Step 1: Batch processing
    for i in range(0, n_features, batch_size):
        batch_features = feature_names[i:i+batch_size]
        X_batch = X[batch_features]

        rfe = RFE(base_estimator, n_features_to_select=n_features_to_select)
        rfe.fit(X_batch, y)

        batch_selected = [f for f, s in zip(batch_features, rfe.support_) if s]
        selected_features.extend(batch_selected)
        print(f"Batch {i//batch_size+1}: selected {batch_selected}")

    # Step 2: Final RFE on combined selected features
    X_final = X[selected_features]
    rfe_final = RFE(base_estimator, n_features_to_select=final_top)
    rfe_final.fit(X_final, y)
    final_selected = [f for f, s in zip(selected_features, rfe_final.support_) if s]

    # Ranking dari final stage
    ranking_df = pd.DataFrame({
        "Feature": selected_features,
        "Ranking": rfe_final.ranking_
    }).sort_values("Ranking")

    print("\n=== Final Selected Features (Batch Mode) ===")
    print(final_selected)
    print("\n=== Feature Rankings (Final Stage) ===")
    display(ranking_df)

    return final_selected, ranking_df

def sfs(
    X, y, 
    base_estimator=None, 
    n_features_to_select=5, 
    direction="forward", 
    scoring=None, 
    cv=5,
    random_state=42
    ):
        """
        Sequential Feature Selection (SFS) for feature selection.
        
        Parameters
        ----------
        X : pd.DataFrame
            Feature matrix.
        y : pd.Series or np.ndarray
            Target values.
        base_estimator : sklearn estimator, optional
            Model to evaluate features. If None, defaults to:
            - RandomForestClassifier for classification
        n_features_to_select : int, default=5
            Number of features to select.
        direction : {"forward", "backward"}, default="forward"
            - "forward": start with 0 features and add one by one
            - "backward": start with all features and remove one by one
        scoring : str or callable, optional
            Scoring metric (e.g., "accuracy", "r2", "f1"). If None, uses default of estimator.
        cv : int, default=5
            Number of cross-validation folds.
        random_state : int, default=42
            Random seed for reproducibility.
        
        Returns
        -------
        dict
            Dictionary with keys:
            - "selected_features" : list List of selected feature names.
            - "support_mask" : np.ndarray Boolean mask of selected features.
        """
    # Default estimator
        if base_estimator is None:       
                base_estimator = RandomForestClassifier(random_state=random_state, n_jobs=-1)

        # SFS
        sfs = SequentialFeatureSelector(
            base_estimator,
            n_features_to_select=n_features_to_select,
            direction=direction,
            scoring=scoring,
            cv=cv,
            n_jobs=-1
        )
        sfs.fit(X, y)

        # results
        support_mask = sfs.get_support()
        selected_features = X.columns[support_mask].tolist()

        print(f"Selected {len(selected_features)} features using SFS ({direction}):")
        print(selected_features)

        return {
        "selected_features": selected_features,
        "support_mask": support_mask
        }

def lasso_feature_selection(X, y, alphas=None, cv=5, top_k=None, random_state=42):
    """
    Lasso-based feature selection with automatic alpha search.
    
    Parameters
    ----------
    X : pd.DataFrame or np.ndarray
        Feature matrix.
    y : pd.Series or np.ndarray
        Target values.
    alphas : list or np.ndarray, optional
        Range of alpha values to search. If None, uses np.logspace(-3, 1, 50).
    cv : int, default=5
        Number of cross-validation folds.
    top_k : int, optional
        Number of top features to keep (ranked by absolute coefficient).
        If None, keep all non-zero features.
    random_state : int, default=42
        Random seed for reproducibility.

    Returns
    -------
    dict
        Dictionary with keys:
        - "selected_features" : list List of selected feature names.
        - "best_alpha" : float Best alpha chosen by cross-validation.
        - "coef_df" : pd.DataFrame DataFrame with features and their coefficients.
    """

    if alphas is None:
        alphas = np.logspace(-3, 1, 50)  # rentang alpha otomatis
    
    # scaling penting buat Lasso
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # cari alpha terbaik dengan cross-validation
    lasso_cv = LassoCV(alphas=alphas, cv=cv, random_state=random_state, n_jobs=-1)
    lasso_cv.fit(X_scaled, y)
    
    best_alpha = lasso_cv.alpha_
    
    # fit ulang dengan alpha terbaik
    lasso = Lasso(alpha=best_alpha, random_state=random_state)
    lasso.fit(X_scaled, y)
    
    # ambil koefisien
    coef = lasso.coef_
    feature_names = X.columns if isinstance(X, pd.DataFrame) else [f"f{i}" for i in range(X.shape[1])]
    
    coef_df = pd.DataFrame({
        "feature": feature_names,
        "coef": coef,
        "abs_coef": np.abs(coef)
    }).sort_values("abs_coef", ascending=False)
    
    # pilih fitur
    if top_k is not None:
        selected_features = coef_df.head(top_k)["feature"].tolist()
    else:
        selected_features = coef_df[coef_df["coef"] != 0]["feature"].tolist()
    
    return {
        "selected_features": selected_features,
        "best_alpha": best_alpha,
        "coef_df": coef_df
    }
