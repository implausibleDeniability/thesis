from collections import defaultdict
from tqdm import tqdm

def extract_top_n_communities(communities: list, n: int=200) -> list[int]:
    community_id2user_list = defaultdict(list)
    for user_description in tqdm(communities):
        user_id = user_description['_id']
        for community_description in user_description['communities']:
            if community_description['type'] == 'profile':
                continue
            community_id = community_description['id']
            community_id2user_list[community_id].append(user_id)
    frequencies = {community_id: len(user_list) for community_id, user_list in community_id2user_list.items()}
    top_n_communities = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)[:n]
    top_n_communities = [community_and_popularity[0] for community_and_popularity in top_n_communities]
    return top_n_communities
