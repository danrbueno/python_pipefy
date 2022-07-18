# Global variables for this project

# GraphQL API URL
API_URL      = "https://api.pipefy.com/graphql"

# User token to access Pipefy.
# You can get this token accessing your account preferences on Pipefy, by:
# - visit https://app.pipefy.com/ 
# - log in to your Pipefy account
# - go to https://app.pipefy.com/tokens
PIPEFY_TOKEN = "PASTE YOUR TOKEN HERE"

# JSON heders
ACCEPT       = "application/json"
CONTENT_TYPE = "application/json"

# Your pipe id (https://app.pipefy.com/pipes/<PIPE_ID>)
PIPE_ID      = "PASTE YOUR PIPE ID HERE"

# The fields of the Pipefy cards you want to extract from GraphQL
EDGES        = "{ edges"
EDGES       += " { node"
EDGES       += " { id title assignees { id } comments { text } comments_count"
EDGES       += " current_phase { name } done due_date fields { name value } labels { name }"
EDGES       += " phases_history { phase { name } firstTimeIn lastTimeOut } url } } pageInfo { endCursor startCursor hasNextPage } }"

