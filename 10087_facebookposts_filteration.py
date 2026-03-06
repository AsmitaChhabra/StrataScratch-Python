https://platform.stratascratch.com/coding/10087-find-all-posts-which-were-reacted-to-with-a-heart?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
facebook_reactions.head()
facebook_posts.head()

fbmerge = pd.merge(facebook_reactions, facebook_posts, left_on = ['poster', 'post_id'], right_on = ['poster', 'post_id'] , how = 'inner') # we can simply do on = instead of left_on and right_on as column names are smake in both dataframes

bmerge.query('reaction == "heart"')

# or 
# fbmerge[fbmerge['reaction'].str.contains('heart')]
