from flask import Flask
app = Flask(__name__)


# TODO: needs tests
@app.route('/event_handler', methods=['POST'])
def hello():
    # TODO: get payload here and hook up to updating the statuses
    # TODO: Integrate with Flask app
    # look up the full name of the repository
    # look  up the last SHA of the pull request
    # payload = JSON.parse(params[:payload])
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
