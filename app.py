from flask import Flask
app = Flask(__name__)


# TODO: needs tests
@app.route('/event_handler', methods=['POST'])
def hello():
    # Check this is the new pull request webhook
    # Set the status to pending (JSON.parse(params[:payload]))
    # Get the commit messages (this would go on a task queue)
    # Run spelling check on the commit messages
    # If passed update status
    # else failed give detailed message (and instructions of how to fix)
    return 'Well, it worked!!!'

# post '/event_handler' do
#   @payload = JSON.parse(params[:payload])

#   case request.env['HTTP_X_GITHUB_EVENT']
#   when "pull_request"
#     if @payload["action"] == "opened"
#       process_pull_request(@payload["pull_request"])
#     end
#   end
# end

# helpers do
#   def process_pull_request(pull_request)
#     puts "It's #{pull_request['title']}"
#   end
# end
