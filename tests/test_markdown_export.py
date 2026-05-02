from pathlib import Path

from Whatsapp_Chat_Exporter.android_handler import create_markdown
from Whatsapp_Chat_Exporter.data_model import ChatStore, Message
from Whatsapp_Chat_Exporter.utility import Device


def _message(*, data, key_id="m1", media=False, mime=None, caption=None):
    msg = Message(from_me=False, timestamp=1700000000, time="12:34", key_id=key_id)
    msg.data = data
    msg.media = media
    msg.mime = mime
    msg.caption = caption
    return msg


def test_create_markdown_writes_chat_file_with_embedded_image_and_copied_asset(tmp_path):
    media_source = tmp_path / "photo.jpg"
    media_source.write_bytes(b"fake image")

    chat = ChatStore(Device.IOS, name="Family/Chat")
    chat.add_message("m1", _message(data="Hello<br>world", key_id="m1"))
    chat.add_message("m2", _message(
        data=str(media_source),
        key_id="m2",
        media=True,
        mime="image/jpeg",
        caption="Holiday photo",
    ))

    create_markdown({"123@s.whatsapp.net": chat}, str(tmp_path / "repo"))

    markdown_file = tmp_path / "repo" / "chats" / "FamilyChat.md"
    copied_asset = tmp_path / "repo" / "assets" / "FamilyChat" / "photo.jpg"

    assert copied_asset.read_bytes() == b"fake image"
    content = markdown_file.read_text(encoding="utf8")
    assert "# Family/Chat" in content
    assert "**123@s.whatsapp.net**" in content
    assert "Hello\nworld" in content
    assert "![Holiday photo](../assets/FamilyChat/photo.jpg)" in content


def test_create_markdown_writes_index_linking_each_chat(tmp_path):
    first = ChatStore(Device.ANDROID, name="Alpha")
    first.add_message("m1", _message(data="one"))
    second = ChatStore(Device.ANDROID, name=None)
    second.add_message("m2", _message(data="two", key_id="m2"))

    create_markdown({"111@s.whatsapp.net": first, "+222@s.whatsapp.net": second}, str(tmp_path / "repo"))

    index = (tmp_path / "repo" / "README.md").read_text(encoding="utf8")

    assert "# WhatsApp Chat Export" in index
    assert "- [Alpha](chats/Alpha.md)" in index
    assert "- [+222@s.whatsapp.net](chats/222s.whatsapp.net.md)" in index
