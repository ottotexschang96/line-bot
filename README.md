# Line Bot Web Application

This is a basic web application built using Flask that integrates with the LINE messaging API. The application listens for incoming messages from users and replies based on pre-defined rule-based logic.

## Features

- Responds to text messages sent by users.
- Sends sticker messages when the word "sticker" is detected in the user's message.
- Handles common greetings and phrases like "hi", "eat", and "who".
- Provides a simple reservation interaction when the user mentions "reserve".

## Technologies Used

- **Python**: Main programming language.
- **Flask**: A lightweight web framework for handling HTTP requests.
- **LINE Messaging API**: Used to send and receive messages from the LINE app.
- **Heroku**: Can be used for deploying the web application (you'll need a Heroku account to deploy).
- **GitHub**: Can be used for storing and versioning your codebase.

## Prerequisites

To run this project locally, you need the following:

- Python 3.x installed
- `pip` (Python package installer)
- LINE Developer account to obtain:
  - `Channel Access Token`
  - `Channel Secret`

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/line-bot-flask.git
   cd line-bot-flask
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set environment variables**:

   You need to set the following environment variables before running the app:

   - `YOUR_CHANNEL_ACCESS_TOKEN`: Your LINE Bot's channel access token.
   - `YOUR_CHANNEL_SECRET`: Your LINE Bot's channel secret.

4. **Run the application**:

   ```bash
   python app.py
   ```

5. **Expose the local server**:

   If you are running the bot locally, you will need to expose the Flask server using tools like `ngrok`:

   ```bash
   ngrok http 5000
   ```

   Use the `ngrok` URL to set up the LINE webhook in your LINE Developer account.

## Deploying to Heroku

1. **Install the Heroku CLI** if you don't have it installed:

   ```bash
   curl https://cli-assets.heroku.com/install.sh | sh
   ```

2. **Login to Heroku**:

   ```bash
   heroku login
   ```

3. **Create a Heroku app**:

   ```bash
   heroku create
   ```

4. **Deploy your application**:

   ```bash
   git push heroku master
   ```

5. **Set Heroku environment variables**:

   ```bash
   heroku config:set YOUR_CHANNEL_ACCESS_TOKEN=your_access_token
   heroku config:set YOUR_CHANNEL_SECRET=your_channel_secret
   ```

6. **Set the LINE webhook URL**:

   After deployment, use the following URL in your LINE Developer account's webhook settings:

   ```
   https://<your-heroku-app-name>.herokuapp.com/callback
   ```

## Usage

Once the app is running, you can interact with the LINE bot by sending messages from the LINE app:

- **Send a greeting**: Type "hi" or "Hi" and the bot will respond.
- **Ask about food**: Type "eat" to get a simple response.
- **Ask who the bot is**: Type "who" to get the bot's response.
- **Send a sticker**: Type "sticker" to receive a sticker from the bot.
- **Make a reservation**: Mention "reserve" to trigger a simple reservation response.
