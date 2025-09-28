# Django Unicom

**Unified communication layer for Django** — easily integrate Telegram bots, WhatsApp bots, and Email bots with a consistent API across all platforms.

## 📑 Table of Contents

- [Quick Start](#-quick-start)
- [Available Platforms](#-available-platforms)
- [Core Models & Usage](#-core-models--usage)
  - [Channel Model](#channel-model)
  - [Message Model](#message-model)
  - [Chat Model](#chat-model)
  - [Template System](#template-system)
  - [Draft Messages & Scheduling](#draft-messages--scheduling)
- [Advanced Features](#-advanced-features)
  - [Email-Specific Features](#email-specific-features)
  - [Telegram-Specific Features](#telegram-specific-features)
  - [LLM Integration](#llm-integration)
  - [Delayed Tool Calls](#delayed-tool-calls)
  - [Message Scheduling](#message-scheduling)
- [Production Setup](#-production-setup)
  - [IMAP Listeners](#imap-listeners)
  - [Scheduled Message Processing](#scheduled-message-processing)
- [Management Commands](#-management-commands)
- [Contributing](#-contributing)
- [License](#-license)
- [Release Automation](#-release-automation)

---

## 🚀 Quick Start

1. **Install the package (plus Playwright browser binaries):**
   ```bash
   pip install django-unicom
   # Install the headless Chromium browser that powers PDF export
   python -m playwright install --with-deps
   ```

2. **Add required apps to your Django settings:**

   ```python
   INSTALLED_APPS = [
       ...
       'django_ace',  # Required for the JSON configuration editor
       'unicom',
   ]
   ```

3. **Include `unicom` URLs in your project's `urls.py`:**

   > This is required so that webhook URLs can be constructed correctly.

   ```python
   from django.urls import path, include

   urlpatterns = [
       ...
       path('unicom/', include('unicom.urls')),
   ]
   ```

4. **Define your public origin:**
   In your Django `settings.py`:

   ```python
   DJANGO_PUBLIC_ORIGIN = "https://yourdomain.com"
   ```

   Or via environment variable:

   ```env
   DJANGO_PUBLIC_ORIGIN=https://yourdomain.com
   ```

5. **Set up media file handling:**
   In your Django `settings.py`:
   ```python
   MEDIA_URL = '/media/'
   MEDIA_ROOT = os.path.join(BASE_DIR, '')
   ```
   In your main project `urls.py`:
   ```python
   from django.conf import settings
   from django.conf.urls.static import static
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```

6. *(Optional, but recommended)* **Set your TinyMCE Cloud API key** — required if you plan to compose **Email** messages from the Django admin UI.

   Obtain a free key at <https://www.tiny.cloud>, then add it to your `settings.py`:

   ```python
   UNICOM_TINYMCE_API_KEY = "your-tinymce-api-key"
   ```

   Or via environment variable:

   ```env
   UNICOM_TINYMCE_API_KEY=your-tinymce-api-key
   ```

   and then you would still have to load it in settings.py

   ```python
   UNICOM_TINYMCE_API_KEY = os.getenv('UNICOM_TINYMCE_API_KEY', '')
   ```

7. *(Optional)* **Set your OpenAI API key** — required if you plan to use the AI-powered template population service.

   Obtain a key from <https://platform.openai.com/api-keys>, then set it as an environment variable:

   ```env
   OPENAI_API_KEY="your-openai-api-key"
   ```

   The application will automatically pick it up from the environment.

8. **Install ffmpeg:**
   - `ffmpeg` is required for converting audio files (e.g., Telegram voice notes) to formats compatible with OpenAI and other services. Make sure `ffmpeg` is installed on your system or Docker image.

That's it! Unicom can now register and manage public-facing webhooks (e.g., for Telegram bots) based on your defined base URL and can automatically sync with email clients.

---

## 📱 Available Platforms

Django Unicom supports the following communication platforms:

- **Email** - SMTP/IMAP with auto-discovery, rich HTML content, link tracking
- **Telegram** - Bot API integration with webhooks, media support, typing indicators
- **WhatsApp** - Business API integration, template messages, delivery status
- **Internal** - System-to-system messaging within your application

Throughout this documentation, features will be marked as:
- ✅ **All platforms**: Works across all communication channels
- 📧 **Email only**: Specific to email channels
- 📱 **Telegram only**: Specific to Telegram channels  
- 💬 **WhatsApp only**: Specific to WhatsApp channels
- 🤖 **LLM features**: AI integration (platform-agnostic)

---

## 📝 Core Models & Usage

### Channel Model

Channels represent communication endpoints for different platforms.

#### Creating Channels Programmatically

```python
from unicom.models import Channel

# Email Channel - Auto-discovers SMTP/IMAP settings
email_channel = Channel.objects.create(
    name="Customer Support Email",
    platform="Email",
    config={
        "EMAIL_ADDRESS": "support@example.com",
        "EMAIL_PASSWORD": "your-app-password"
    }
)

# Email Channel - Custom SMTP/IMAP settings
email_channel_custom = Channel.objects.create(
    name="Marketing Email", 
    platform="Email",
    config={
        "EMAIL_ADDRESS": "marketing@example.com",
        "EMAIL_PASSWORD": "password",
        "IMAP": {
            "host": "imap.example.com",
            "port": 993,
            "use_ssl": True,
            "protocol": "IMAP"
        },
        "SMTP": {
            "host": "smtp.example.com", 
            "port": 587,
            "use_ssl": True,
            "protocol": "SMTP"
        },
        "TRACKING_PARAMETER_ID": "utm_source",  # 📧 Custom tracking parameter
        "MARK_SEEN_WHEN": "on_request_completed"  # 📧 When to mark emails as seen
    }
)

# Telegram Channel - Auto-generates webhook secret
telegram_channel = Channel.objects.create(
    name="Customer Bot",
    platform="Telegram", 
    config={
        "API_TOKEN": "your-bot-token-from-botfather"
    }
)

# Validate channel (sets up webhooks/connections)
channel.validate()  # Returns True if successful
```

#### Creating Channels via Admin Interface

1. Go to Django Admin > Unicom > Channels
2. Click "Add Channel"
3. Fill in the name, select platform, and add configuration JSON
4. Save - the channel will automatically validate and set up webhooks

#### Sending Messages with Channels

```python
# ✅ All platforms: Basic message sending
message = channel.send_message({
    'chat_id': 'recipient_chat_id',
    'text': 'Hello from Django Unicom!'
})

# 📧 Email only: New email thread
message = email_channel.send_message({
    'to': ['recipient@example.com'],
    'subject': 'Welcome!',
    'html': '<h1>Welcome to our service!</h1>'
})

# 📧 Email only: Email with CC/BCC
message = email_channel.send_message({
    'to': ['primary@example.com'],
    'cc': ['manager@example.com'],
    'bcc': ['archive@example.com'], 
    'subject': 'Team Update',
    'html': '<p>Here is the latest update...</p>'
})

# 📧 Email only: Reply to existing email thread
message = email_channel.send_message({
    'chat_id': 'existing_email_thread_id',
    'html': '<p>Thanks for your message!</p>'
    # Subject is automatically derived from thread
})
```

### Message Model

Messages represent individual communications across all platforms with rich metadata and tracking capabilities.

#### Key Message Fields by Platform

The Message model contains many important fields that provide detailed information about message status, tracking, and content. **Important:** Each field is only populated by specific platforms:

```python
from unicom.models import Message

# Content fields (✅ All platforms)
message.text          # Plain text content  
message.sender_name   # Display name of sender
message.timestamp     # When message was created
message.is_outgoing   # True=outgoing, False=incoming, None=system
message.platform      # 'Email', 'Telegram', 'WhatsApp', 'Internal'
message.media_type    # 'text', 'html', 'image', 'audio', 'tool_call', 'tool_response'
message.media         # Attached media file
message.raw           # Raw platform-specific data (JSON)

# 📧 Email-only content fields
message.html          # HTML content
message.subject       # Email subject line  
message.to            # List of recipient email addresses (array)
message.cc            # List of CC email addresses (array)
message.bcc           # List of BCC email addresses (array)
message.imap_uid      # IMAP UID for server operations

# 💬 WhatsApp-only status tracking
message.sent          # Updated when WhatsApp confirms message sent
message.delivered     # Updated when WhatsApp confirms message delivered
message.seen          # Updated when WhatsApp confirms message read
message.time_sent     # When WhatsApp confirmed message sent
message.time_delivered # When WhatsApp confirmed message delivered  
message.time_seen     # When WhatsApp confirmed message read

# 📧 Email-only tracking (via tracking pixels & links)
message.opened        # Set to True when recipient opens email
message.time_opened   # When email was first opened (via tracking pixel)
message.link_clicked  # Set to True when any tracked link is clicked
message.time_link_clicked # When first link was clicked
message.clicked_links # Array of all URLs that have been clicked
message.tracking_id   # UUID used for tracking pixel and link tracking
```

#### Platform-Specific Usage Examples

```python
# 💬 WhatsApp: Check delivery status (only WhatsApp provides this data)
whatsapp_msg = Message.objects.get(id='whatsapp_message_id')
if whatsapp_msg.delivered:
    print(f"WhatsApp message delivered at: {whatsapp_msg.time_delivered}")
if whatsapp_msg.seen:
    print(f"WhatsApp message read at: {whatsapp_msg.time_seen}")

# 📧 Email: Check tracking data (only emails have open/click tracking)  
email_msg = Message.objects.get(id='email_message_id')
if email_msg.opened:
    print(f"Email opened at: {email_msg.time_opened}")
if email_msg.link_clicked:
    print(f"Links clicked: {email_msg.clicked_links}")
    print(f"First click at: {email_msg.time_link_clicked}")

# ✅ All platforms: Basic message info
for message in Message.objects.filter(channel=channel):
    print(f"{message.platform}: {message.sender_name} - {message.text}")
    if message.is_outgoing:
        print("  (Outgoing message)")
    elif message.is_outgoing is False:
        print("  (Incoming message)")  
    else:
        print("  (System message)")

# 💬 WhatsApp-specific queries
unread_whatsapp = Message.objects.filter(
    platform='WhatsApp',
    is_outgoing=True,
    seen=False  # Only WhatsApp populates this field
)

# 📧 Email-specific queries  
opened_emails = Message.objects.filter(
    platform='Email',
    opened=True  # Only emails have open tracking
)

clicked_emails = Message.objects.filter(
    platform='Email', 
    link_clicked=True  # Only emails have click tracking
).values('subject', 'clicked_links', 'time_link_clicked')
```

#### Understanding Field Limitations

**Important Notes:**
- **Delivery tracking** (`delivered`, `time_delivered`): Only WhatsApp provides delivery confirmations
- **Read tracking** (`seen`, `time_seen`): Only WhatsApp provides read receipts  
- **Email open tracking** (`opened`, `time_opened`): Only works when recipient loads images/tracking pixels
- **Email click tracking** (`link_clicked`, `time_link_clicked`, `clicked_links`): Only works for links that go through tracking system
- **Email "seen" status**: Use `imap_uid` field and IMAP operations, not the `seen` field

#### Accessing Messages

```python
from unicom.models import Message

# Get message by ID
message = Message.objects.get(id='message_id')

# Get recent messages for a channel
recent_messages = Message.objects.filter(
    channel=channel
).order_by('-timestamp')[:10]

# Get conversation history
chat_messages = Message.objects.filter(
    chat_id='chat_id'
).order_by('timestamp')
```

#### Replying to Messages

```python
# ✅ All platforms: Reply with text
reply = message.reply_with({
    'text': 'Thanks for your message!'
})

# 📧 Email only: Reply with HTML
reply = message.reply_with({
    'html': '<p>Thank you for contacting us!</p><p>We will get back to you soon.</p>'
})

# ✅ All platforms: Reply with media
reply = message.reply_with({
    'text': 'Here is the file you requested',
    'file_path': '/path/to/file.pdf'
})
```

#### Via Admin Interface

1. Go to Django Admin > Unicom > Messages  
2. Find the message you want to reply to
3. Click on the message ID to open details
4. Use the "Reply" button in the interface
5. Compose your reply using the rich text editor (📧 email) or plain text

### Chat Model

Chats represent conversations/threads across platforms.

#### Working with Chats

```python
from unicom.models import Chat

# Get chat by ID
chat = Chat.objects.get(id='chat_id')

# Send message to chat
message = chat.send_message({
    'text': 'Hello everyone!'
})

# 📧 Email only: Reply to last incoming message in email thread
reply = chat.send_message({
    'html': '<p>Following up on our previous conversation...</p>'
})

# Reply to specific message in chat
reply = chat.send_message({
    'reply_to_message_id': 'specific_message_id',
    'text': 'Replying to your specific question...'
})
```

### Template System

Create reusable message templates for consistent communication.

#### Creating Templates Programmatically

```python
from unicom.models import MessageTemplate

# Create a basic template
template = MessageTemplate.objects.create(
    title='Welcome Email',
    content='<h1>Welcome {{name}}!</h1><p>Thank you for joining {{company}}.</p>',
    category='Onboarding'
)

# Make template available for specific channels
template.channels.add(email_channel)
template.channels.add(telegram_channel)

# 🤖 AI-powered template population (requires OpenAI API key)
populated_content = template.populate(
    html_prompt="User name is John Doe, company is Acme Corp",
    model="gpt-4"
)
```

#### Creating Templates via Admin Interface

1. Go to Django Admin > Unicom > Message Templates
2. Click "Add Message Template" 
3. Fill in title, description, category
4. Create your HTML content using TinyMCE editor (📧 email templates get rich editor)
5. Select which channels can use this template
6. Save template

#### Using Templates in Messages

```python
# Get template and use its content
template = MessageTemplate.objects.get(title='Welcome Email')

# Use template content directly
message = channel.send_message({
    'to': ['newuser@example.com'],
    'subject': 'Welcome!', 
    'html': template.content.replace('{{name}}', 'John Doe')
})

# Or use AI population
populated = template.populate("User is John Doe from Acme Corp")
message = channel.send_message({
    'to': ['john@acme.com'],
    'subject': 'Welcome!',
    'html': populated
})
```

### Draft Messages & Scheduling

Create draft messages and schedule them for later sending.

#### Creating Draft Messages

```python
from unicom.models import DraftMessage
from django.utils import timezone

# Create a scheduled email
draft = DraftMessage.objects.create(
    channel=email_channel,
    to=['customer@example.com'],
    subject='Weekly Newsletter', 
    html='<h1>This week\'s updates...</h1>',
    send_at=timezone.now() + timezone.timedelta(hours=24),
    is_approved=True,
    status='scheduled'
)

# Create a Telegram draft  
telegram_draft = DraftMessage.objects.create(
    channel=telegram_channel,
    chat_id='telegram_chat_id',
    text='Scheduled announcement for tomorrow',
    send_at=timezone.now() + timezone.timedelta(days=1),
    is_approved=True,
    status='scheduled'
)

# Send draft immediately (if approved and time has passed)
sent_message = draft.send()
```

#### Creating Drafts via Admin Interface

1. Go to Django Admin > Unicom > Draft Messages
2. Click "Add Draft Message"
3. Select channel and fill in recipient details
4. Compose message content
5. Set "Send at" time for scheduling
6. Mark as "Approved" when ready to send  
7. Status will automatically update to "Scheduled"

---

## 🚀 Advanced Features

### Email-Specific Features

#### 📧 Link Tracking

Email channels automatically track which links recipients click:

```python
# Send email with trackable links
message = email_channel.send_message({
    'to': ['user@example.com'], 
    'subject': 'Check out our new features',
    'html': '''
        <p>Visit our <a href="https://example.com/features">features page</a></p>
        <p>Or check the <a href="https://example.com/docs">documentation</a></p>
    '''
})

# Check tracking data later
if message.link_clicked:
    print(f"First link clicked at: {message.time_link_clicked}")
    print(f"Clicked links: {message.clicked_links}")

if message.opened:
    print(f"Email opened at: {message.time_opened}")
```

#### 📧 Rich HTML Content with TinyMCE

The admin interface provides a rich text editor for composing HTML emails with features like:
- Font formatting, colors, styles
- Image uploads and inline images
- Tables, lists, links
- Template insertion
- AI-powered content generation

#### 📧 DKIM and SPF Verification

Email channels automatically validate DKIM and SPF records for incoming messages, ensuring email authenticity and preventing spoofing.

### Telegram-Specific Features

#### 📱 Typing Indicators

```python
from unicom.services.telegram import start_typing_in_telegram, stop_typing_in_telegram

# Show typing indicator
start_typing_in_telegram(telegram_channel, chat_id="telegram_chat_id")

# Your processing logic here
import time
time.sleep(2)

# Stop typing and send message  
stop_typing_in_telegram(telegram_channel, chat_id="telegram_chat_id")
message = telegram_channel.send_message({
    'chat_id': 'telegram_chat_id',
    'text': 'Here is your response!'
})
```

#### 📱 File Downloads and Voice Messages

Telegram channels automatically handle file downloads and voice message processing:

```python
# Voice messages are automatically converted to compatible formats
# and can be processed by LLM services
if message.media_type == 'audio':
    # Voice message is available in message.media
    # Converted to MP3 format for compatibility
    llm_response = message.reply_using_llm(
        model="gpt-4-vision-preview", 
        multimodal=True  # Enables audio processing
    )
```

### LLM Integration

#### 🤖 AI-Powered Responses (Platform-Agnostic)

```python
# Basic LLM reply to any message
response = message.reply_using_llm(
    model="gpt-4",
    system_instruction="You are a helpful customer service assistant",
    depth=10  # Include last 10 messages for context
)

# 🤖 Multimodal support (images, audio)
response = message.reply_using_llm(
    model="gpt-4-vision-preview",
    multimodal=True,  # Process images and audio
    voice="alloy"  # Voice for audio responses
)
```

#### 🤖 Tool Call System

The LLM system can call external functions and tools:

```python
# Log tool interactions
message.log_tool_interaction(
    tool_call={
        "name": "search_database", 
        "arguments": {"query": "user orders", "limit": 5},
        "id": "call_123"
    }
)

# Log tool response
message.log_tool_interaction(
    tool_response={
        "call_id": "call_123",
        "result": {"orders": [...], "count": 3}
    }
)

# Get LLM-ready conversation including tool calls
conversation = message.as_llm_chat(depth=20, mode="chat")
```

#### 🤖 Chat-Level Tool Interactions

```python
# System-initiated tool call
chat.log_tool_interaction(
    tool_call={"name": "cleanup_cache", "arguments": {}, "id": "call_456"}
)

# With specific reply target
chat.log_tool_interaction(
    tool_call={"name": "fetch_data", "arguments": {"user_id": 123}, "id": "call_789"},
    reply_to=some_message
)
```

### Delayed Tool Calls

#### 🤖 Request-Based Tool Call Management

The LLM system supports delayed tool calls that can take hours or days to complete, perfect for reminders, monitoring, and long-running processes.

```python
from unicom.models import Request, ToolCall

# Submit multiple tool calls from a request (atomic operation)
request = Request.objects.get(id='request_id')
tool_calls = request.submit_tool_calls([
    {
        "name": "set_reminder",
        "arguments": {"text": "Meeting tomorrow", "delay_hours": 24},
        "id": "call_123"  # Optional, auto-generated if omitted
    },
    {
        "name": "monitor_system", 
        "arguments": {"threshold": 90}
    }
])

# Days later... respond to tool calls
reminder_call = ToolCall.objects.get(call_id="call_123")
msg, child_request = reminder_call.respond("Reminder: Meeting in 1 hour")
# Creates new child request for further processing

# For periodic/ongoing tools, set status to ACTIVE
monitor_call = tool_calls[1]  
monitor_call.status = 'ACTIVE'
monitor_call.save()
# Now it can respond indefinitely without creating child requests
monitor_call.respond("CPU usage: 95%")  # Just logs, no child request
monitor_call.respond("CPU usage: 92%")  # Just logs, no child request
```

#### 🤖 Request Hierarchy and Final Response Logic

```python
# Only when ALL pending tool calls respond does system create child request
request = Request.objects.get(id='parent_request')

# Submit 3 tool calls
calls = request.submit_tool_calls([
    {"name": "search", "arguments": {"query": "data"}},
    {"name": "analyze", "arguments": {"input": "results"}}, 
    {"name": "report", "arguments": {"format": "pdf"}}
])

# Respond to each (no child request yet)
calls[0].respond("search results")     # No child - not final
calls[1].respond("analysis complete")  # No child - not final  
calls[2].respond("report generated")   # Child request created!

# Child request inherits context from initial request
child = Request.objects.filter(parent_request=request).first()
print(f"Child inherits: {child.account}, {child.category}, {child.member}")
```

#### 🤖 Request Tracking Fields

New fields added to Request model for LLM and tool call tracking:

```python
request.parent_request     # Parent request that spawned this one
request.initial_request    # Root request that started the chain
request.tool_call_count    # Number of tool calls made from this request
request.llm_calls_count    # Number of LLM API calls made
request.llm_token_usage    # Total tokens consumed by LLM
```

### Message Scheduling

#### Automated Scheduling System

```python
# Check and process scheduled messages manually
from unicom.services.crossplatform.scheduler import process_scheduled_messages

result = process_scheduled_messages()
print(f"Processed {result['total_due']} messages")
print(f"Sent: {result['sent']}, Failed: {result['failed']}")
```

---

## ⚙️ Production Setup

### IMAP Listeners

Email channels require IMAP listeners to receive incoming emails in real-time.

#### Development (Django runserver)
When using `python manage.py runserver`, IMAP listeners start automatically with the server.

#### Production (Gunicorn, uWSGI, etc.)
In production deployments, you need to run IMAP listeners as a separate process:

```bash
# Start IMAP listeners for all active email channels
python manage.py start_imap_listeners
```

This command will:
- Start IMAP IDLE connections for all active email channels
- Keep running until stopped with Ctrl+C
- Automatically reconnect if connections drop
- Process incoming emails in real-time

#### Docker/Containerized Deployments

Add a separate service in your `docker-compose.yml`:

```yaml
services:
  web:
    # Your main Django app
    
  imap_listener:
    # Same image as your web service  
    build: .
    command: python manage.py start_imap_listeners
    volumes:
      - .:/app
    environment:
      # Same environment as web service
    depends_on:
      - db
```

### Scheduled Message Processing

For automated sending of scheduled messages:

```bash
# Process scheduled messages every 10 seconds (default)
python manage.py send_scheduled_messages

# Custom interval (30 seconds)  
python manage.py send_scheduled_messages --interval 30
```

Add this as a background service or cron job in production.

---

## 🛠️ Management Commands

Available management commands for production and development:

### `start_imap_listeners`
Starts IMAP listeners for all active email channels. Required in production when not using `runserver`.

```bash
python manage.py start_imap_listeners
```

### `send_scheduled_messages` 
Continuously processes and sends scheduled messages.

```bash
# Default 10-second interval
python manage.py send_scheduled_messages

# Custom interval
python manage.py send_scheduled_messages --interval 30
```

### `run_as_llm_chat`
Triggers an LLM response to a specific message (useful for testing AI features).

```bash  
python manage.py run_as_llm_chat <message_id>
```

---

## 🧑‍💻 Contributing

We ❤️ contributors!

### Requirements:

* Docker & Docker Compose installed

### Getting Started:

1. Clone the repo:

   ```bash
   git clone https://github.com/meena-erian/unicom.git
   cd unicom
   ```

2. Create a `db.env` file in the root:

   ```env
   POSTGRES_DB=unicom_test
   POSTGRES_USER=unicom
   POSTGRES_PASSWORD=unicom
   DJANGO_PUBLIC_ORIGIN=https://yourdomain.com
   # Needed if you want to use the rich-text email composer in the admin
   UNICOM_TINYMCE_API_KEY=your-tinymce-api-key
   # Needed if you want to use the AI template population service
   OPENAI_API_KEY=your-openai-api-key
   ```

3. Start the dev environment:

   ```bash
   docker-compose up --build
   ```

4. Run tests:

   ```bash
   docker-compose exec app pytest
   ```

   or just

   ```bash
   pytest
   ```
   Note: To run ```test_telegram_live``` tests you need to create ```telegram_credentials.py``` in the tests folder and define in it ```TELEGRAM_API_TOKEN``` and ```TELEGRAM_SECRET_TOKEN``` and to run ```test_email_live``` you need to create ```email_credentials.py``` in the tests folder and define in it ```EMAIL_CONFIG``` dict with the properties ```EMAIL_ADDRESS```: str, ```EMAIL_PASSWORD```: str, and ```IMAP```: dict, and ```SMTP```: dict, each of ```IMAP``` and ```SMTP``` contains ```host```:str ,```port```:int, ```use_ssl```:bool, ```protocol```: (```IMAP``` | ```SMTP```)  

No need to modify `settings.py` — everything is pre-wired to read from `db.env`.

---

## 📄 License

MIT License © Meena (Menas) Erian

## 📦 Release Automation

To release a new version to PyPI:

1. Ensure your changes are committed and pushed.
2. Run:
   
   ```bash
   make release VERSION=1.2.3
   ```
   This will:
   - Tag the release as v1.2.3 in Git
   - Push the tag
   - Build the package
   - Upload to PyPI using your .pypirc

3. For an auto-generated version based on date/time, just run:
   
   ```bash
   make release
   ```
   This will use the current date/time as the version (e.g., 2024.06.13.1530).

The version is automatically managed by setuptools_scm from Git tags and is available at runtime as `unicom.__version__`.