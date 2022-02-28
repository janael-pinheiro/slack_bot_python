<h1>Slack bot in python</h1>
To interact with Slack through Python, you'll need to create a workspace if you don't have access to one, as well as an Slack application.

<br>
<h3> Create a Slack workspace </h3>
Access https://slack.com/intl/pt-br/get-started#/createnew to create a new workspace.

<br>
<h3> Create App in Slack </h3>
<p>To create an app, go to https://api.slack.com/apps. Then click "Create New App". Select "From scratch". Give it a name and choose a workspace. Click "Create App". Go to the permissions card. In the "Scopes" section, "Bot Token Scopes" subsection, click "Add an OAuth Scope". Type "chat:write", which allows the bot to write to channels it has access to.</p>

<p>Return to the "OAuth Tokens for Your Workspace" section and click "Install to Workspace". Finally, click "Allow". In the "OAuth Tokens for Your Workspace" section, you'll have access to the token used to authenticate to Slack. Copy and save the token for later use.</p>

<p>The last configuration step is to add the application to one or more channels. In the Slack desktop or web app, click your app in the "Apps" section. At the top of the screen, click your app's name. Click "Add this app to a channel". Select the channel. Done, now you can use the bot to send messages to the selected channel.</p>

<br>
<h3>Create Docker image</h3>
$sudo docker build -t slack_bot . -f Docker/Dockerfile --build-arg SLACK_TOKEN="slack_token"

<br>
<h3>Test the bot</h3>

The application consists of a REST service that receives the channel and message at the "/send_message" endpoint, then relays the message to Slack. Usage: python3 src/service/application.py.

$curl -d '{"channel":"channel_name", "message":"message content"}' -H "Content-Type: application/json" -X POST http://localhost:8080/send_message