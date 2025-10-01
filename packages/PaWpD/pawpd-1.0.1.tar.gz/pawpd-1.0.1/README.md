# Hello welcome to PaWpD.

Changelog for 1.0.1

## What's changed?
The package's files were cleaned off debug files and fixed issue with dependencies not getting installed when installing package. Also added Docs and moved project files on GitHub. Btw 1.1.0 really soon. It's actually ready just needs docs. 1.2.0 is already in development.

### What's PaWpD?
PaWpD is a package for creating discord bots. PaWpD is a minimal client made for performance and low latencies. 

### How to use PaWpD?

It's supper easy!

First import the package
```python
import pawpd 
```
Then initialize the client
```python
client = pawpd.Client(token="Your discord token")
```
And start it!
```python
client.start()
```
And that's all. PaWpD client should be now implemented!

#### Warning by default PaWpD client uses all client intents if you haven't passed intents thru client value. Currently 1.0.0 version has no way of setting other intents than all thru client. It has to be manually passed. Example:
```python
### All intents
client = pawpd.Client(token=token, intents=pawpd.intents.all())
### Any other intents must be passed manually 
client = pawpd.Client(token=token, intents="intent number here")
```
More Intents should be implemented in next update.

Now if you want to implement commands. All you have to do is:
(Assuming the implementation above was used)
```python
@client.command()
async def hi(msg):
    await msg.send("Hello")
```
#### WARNING: In order for client commands to work. You have to pass prefix value in client.
```python
client = pawpd.Client(token="discord token", prefix="Whatever prefix you want your bot responding to")
```
And that's all. You should now have a command called hi which returns Hello.

PaWpD client comes with built-in help command. Which you can call by !help (assuming bot prefix is !)

Built-in help command lists all bot commands no matter if they are slash, hybrid.

Built-in help command can be disabled by passing:
```python
builtin_help=False
```
In client function.

Implementing slash/hybrid commands

Implementing these commands is super easy. This is the benefits of PaWpD.

All you have to do is pass slash or hybrid value in command:
```python
### normally 
@client.command()
### hybrid command
@client.command(hybrid=True)
### slash command
@client.command(slash=True)
```

#### WARNING: Interaction commands (slash/hybrid) needs to he synced to show up as slash commands. It can be done by:
```python
await client.sync()
# or
await client.sync(guild_ids=["ids here"])
# to sync to specific guilds
```

The only difference between normal commands and slash/hybrid is that it allows you to use 
```python
await msg.defer()
```
Also in order to respond on slash command. You have to:
```python
await msg.reply(message)
# This Replies on interaction. Meanwhile
await msg.send(message)
# This doesn't respond on interaction. It sends a new message in channel and keeps the interaction as not responded to.
```

### How to implement an event in PaWpD

That's also super easy
```python
@client.event
async def on_ready(user):
    # User value is Bot User that we just had logged on.
    print(f"Logged in as {user.username}")
    # This also shows how to get bot Latency. This function tests latency on your command thats why its a function and it needs to be awaited
    latency = await client.latency()
    print(latency) # Latency is returned in Milliseconds in Float value
```
That's how you can implement on_ready event.
This is a list of events 
on_ready, on_member_join, on_member_leave, on_guild_update, on_guild_join, on_guild_leave, on_message_create, on_message_update, on_message_delete

The value passed for events are the same as their second word from name. Example
on_member_join
Second word is member. So member is passed. Same for rest.

### How to make Embeds with PaWpD

It's easy!
```python
embed = pawpd.Embed(title=title, description=description, color=pawpd.Color.Gray())
### Example add Field
embed.add_field(name=name, value=value, inline=True)
### Example set footer
embed.set_footer(text=text, icon_url=url)
### Example set author
embed.set_author(author=author, url=url, icon_url=icon_url) # Url value will be removed in next version. I hope...
# Author value may be changed to name in next update!
```
Now to send an embed
```python
await msg.send(embed=embed)
# or embeds if multiple
await msg.send(embeds=[embed, embed2])
```

Every value is nearly same for any functions.
Have fun using PaWpD. We hope this project will grow big and you will like it!