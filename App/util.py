def get_results(movie_id):
    import numpy as np
    import pandas as pd
    from scipy.sparse import csr_matrix
    from sklearn.metrics.pairwise import cosine_similarity

    movie_df = pd.read_csv('D:\\PRML project\\Dataset\\movies.csv')
    rating_df = pd.read_csv('D:\\PRML project\\Dataset\\ratings.csv')

    movie_stats = rating_df.groupby('movieId')['rating'].agg(['count', 'mean'])
    C = movie_stats['count'].mean() #Average number of ratings for a given movie
    m = movie_stats['mean'].mean() #Average rating for a given movie

    def bayesian_avg(ratings):
        bayesian_avg = (C*m+ratings.sum())/(C+ratings.count())
        return round(bayesian_avg, 3)
    bayesian_avg_ratings = rating_df.groupby('movieId')['rating'].agg(bayesian_avg).reset_index()
    bayesian_avg_ratings.columns = ['movieId', 'bayesian_avg']
    movie_stats = movie_stats.merge(bayesian_avg_ratings, on='movieId')
    movie_stats = movie_stats.merge(movie_df[['movieId', 'title']])
    movie_stats.sort_values('bayesian_avg', ascending=False)
    movie_df['genres'] = movie_df['genres'].apply(lambda x: x.split("|"))

    def create_X(df):
        M = df['userId'].nunique()
        N = df['movieId'].nunique()

        user_mapper = dict(zip(np.unique(df["userId"]), list(range(M))))
        movie_mapper = dict(zip(np.unique(df["movieId"]), list(range(N))))
        
        user_inv_mapper = dict(zip(list(range(M)), np.unique(df["userId"])))
        movie_inv_mapper = dict(zip(list(range(N)), np.unique(df["movieId"])))
        
        user_index = [user_mapper[i] for i in df['userId']]
        item_index = [movie_mapper[i] for i in df['movieId']]

        X = csr_matrix((df["rating"], (user_index,item_index)), shape=(M,N))
        
        return X, user_mapper, movie_mapper, user_inv_mapper, movie_inv_mapper

    X, user_mapper, movie_mapper, user_inv_mapper, movie_inv_mapper = create_X(rating_df)

    #TODO: Use X for dumping

    from sklearn.neighbors import NearestNeighbors

    def find_similar_movies(movie_id, X, movie_mapper, movie_inv_mapper, k=50, metric='cosine'):
        X = X.T
        neighbour_ids = []
        
        movie_ind = movie_mapper[movie_id]
        movie_vec = X[movie_ind]
        if isinstance(movie_vec, (np.ndarray)):
            movie_vec = movie_vec.reshape(1,-1)
        # use k+1 since kNN output includes the movieId of interest
        kNN = NearestNeighbors(n_neighbors=k+1, algorithm="brute", metric=metric)
        kNN.fit(X)
        neighbour = kNN.kneighbors(movie_vec, return_distance=False)
        for i in range(0,k):
            n = neighbour.item(i)
            neighbour_ids.append(movie_inv_mapper[n])
        neighbour_ids.pop(0)
        return neighbour_ids

    similar_movies = find_similar_movies(1, X, movie_mapper, movie_inv_mapper,k=50)
    movie_titles = dict(zip(movie_df['movieId'], movie_df['title']))

    similar_movies = find_similar_movies(movie_id, X, movie_mapper, movie_inv_mapper, metric='cosine', k=60)

    collaboration_filter_list = similar_movies

    genres = set(g for G in movie_df['genres'] for g in G)
    for g in genres:
        movie_df[g] = movie_df.genres.transform(lambda x: int(g in x))
    movie_genres = movie_df.drop(columns=['movieId', 'title','genres'])
    cosine_sim = cosine_similarity(movie_genres, movie_genres)

    #TODO: Use cosin_sim for dumping 

    movie_idx = dict(zip(movie_df['movieId'], list(movie_df.index)))

    def get_content_based_recommendations(movie_id, n_recommendations=50):
        idx = movie_idx[movie_id]
        title = movie_df.loc[idx, 'title']
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:(n_recommendations+1)]
        similar_movies_idx = [i[0] for i in sim_scores]
        similar_movie_ids = movie_df.loc[similar_movies_idx, 'movieId'].tolist()
        return similar_movie_ids

    content_based_list = get_content_based_recommendations(movie_id, 60)

    import random

    common_elements = list(set(content_based_list) & set(collaboration_filter_list))

    movie_id_to_title = dict(zip(movie_df['movieId'], movie_df['title']))

    num_common_elements = len(common_elements)
    num_random = max(0, 10 - num_common_elements)

    # Generate random elements
    random_elements_from_list = random.sample(content_based_list, num_random)

    # Remove random elements from common_elements before adding them to final_elements
    common_elements = [elem for elem in common_elements if elem not in random_elements_from_list]

    final_elements = common_elements + random_elements_from_list
    if len(final_elements) > 10:
        final_elements = final_elements[:10]

    # Create a list of tuples containing both the title and movie ID
    hybrid = [(movie_id, movie_id_to_title[movie_id]) for movie_id in final_elements]

    # Optionally, if you want to sort hybrid based on movie IDs:
    hybrid.sort(key=lambda x: x[0])

    movie_idx = dict(zip(movie_df['movieId'], list(movie_df.index)))
    return hybrid
