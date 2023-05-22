import numpy as np
from tqdm import tqdm

from src.preprocessing.extract_top_n_communities import extract_top_n_communities


class CommunitySubscriptionMatrixBuilder:
    def build(self, communities: dict, public_user_id_to_research_id: dict[int, int], top_n: int=300) -> np.ndarray:
        top_n_communities = extract_top_n_communities(communities, top_n)
        user_id2community_id_list = self._build_user_id2community_id_list(communities)
        community_binary_matrix = np.zeros((len(public_user_id_to_research_id), len(top_n_communities)))
        for user_id in tqdm(user_id2community_id_list):
            research_user_id = public_user_id_to_research_id[user_id]
            for j, community_id in enumerate(top_n_communities):
                if community_id in user_id2community_id_list[user_id]:
                    community_binary_matrix[research_user_id, j] = 1
        return community_binary_matrix
                                                
    def _build_user_id2community_id_list(self, communities: dict) -> dict[int, list]:
        user_id2community_id_list = {
            user_description['_id']: [
                community_description['id'] for community_description in user_description['communities']
            ]
            for user_description in communities
        }
        return user_id2community_id_list
