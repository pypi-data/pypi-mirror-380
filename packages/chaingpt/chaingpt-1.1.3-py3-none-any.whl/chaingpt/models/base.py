from pydantic import BaseModel


class ChatBotModel(BaseModel):
    """Model for chatbot information in chat history."""

    name: str
    description: str
    createdAt: str
    fileDescriptor: str


class UserModel(BaseModel):
    """Model for user information in chat history."""

    firstName: str | None = None
    lastName: str | None = None
    email: str
    createdAt: str
    profilePictureId: str | None = None
    profilePicture: str | None = None
