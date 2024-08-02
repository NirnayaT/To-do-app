
html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WebSocket Text Display</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
        }
        .message {
            font-size: 2em;
            color: #333;
        }
    </style>
</head>
<body>
    <div class="message" id="message">Connecting...</div>

    <script>
        // Create a WebSocket connection
        const ws = new WebSocket('ws://localhost:8000/ws/message');

        // Handle the WebSocket connection open event
        ws.onopen = () => {
            console.log('WebSocket connection established');
        };

        // Handle incoming WebSocket messages
        ws.onmessage = (event) => {
            const messageDiv = document.getElementById('message');
            messageDiv.innerText = event.data; // Display the received message
        };

        // Handle WebSocket connection close event
        ws.onclose = () => {
            const messageDiv = document.getElementById('message');
            messageDiv.innerText = 'Connection closed'; // Notify user
        };

        // Handle WebSocket errors
        ws.onerror = (error) => {
            const messageDiv = document.getElementById('message');
            messageDiv.innerText = 'Error: ' + error.message; // Show error message
            console.error('WebSocket error:', error);
        };
    </script>
</body>
</html>
"""


# html = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>WebSocket Text Display</title>
#     <style>
#         body {
#             display: flex;
#             flex-direction: column;
#             justify-content: center;
#             align-items: center;
#             height: 100vh;
#             font-family: Arial, sans-serif;
#             background-color: #f0f0f0;
#         }
#         .message {
#             font-size: 2em;
#             color: #333;
#         }
#         #comments {
#             margin-top: 20px;
#             width: 80%;
#             max-width: 600px;
#         }
#         .comment {
#             padding: 10px;
#             margin: 5px 0;
#             background-color: #fff;
#             border-radius: 5px;
#             box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
#         }
#     </style>
# </head>
# <body>
#     <div class="message" id="message">Connecting...</div>
#     <div id="comments"></div>
#     <input type="text" id="comment" placeholder="Type your comment here" />
#     <button onclick="sendComment()">Send Comment</button>

#     <script>
#         // Create a WebSocket connection
#         const ws = new WebSocket('ws://localhost:8000/ws/comments');

#         // Handle the WebSocket connection open event
#         ws.onopen = () => {
#             console.log('WebSocket connection established');
#             const messageDiv = document.getElementById('message');
#             messageDiv.innerText = 'Connected';
#         };

#         // Handle incoming WebSocket messages
#         ws.onmessage = (event) => {
#             console.log('Received message:', event.data);  // Debugging line
#             const commentsDiv = document.getElementById('comments');
#             const comment = document.createElement('div');
#             comment.className = 'comment';
#             comment.textContent = event.data;
#             commentsDiv.appendChild(comment);
#         };

#         // Handle WebSocket connection close event
#         ws.onclose = () => {
#             const messageDiv = document.getElementById('message');
#             messageDiv.innerText = 'Connection closed'; // Notify user
#         };

#         // Handle WebSocket errors
#         ws.onerror = (error) => {
#             const messageDiv = document.getElementById('message');
#             messageDiv.innerText = 'Error: ' + error.message; // Show error message
#             console.error('WebSocket error:', error);
#         };

#         // Function to send a comment
#         function sendComment() {
#             const commentInput = document.getElementById('comment');
#             const comment = {
#                 task_id: 1, // Example task_id, replace with the actual task_id
#                 comment: commentInput.value,
#                 user_id: 1  // Example user_id, replace with the actual user_id
#             };
#             console.log('Sending comment:', comment);  // Debugging line
#             ws.send(JSON.stringify(comment));
#             commentInput.value = '';
#         }
#     </script>
# </body>
# </html>
# """
