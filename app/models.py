from sqlalchemy import (
    Column,
    Boolean,
    Integer,
    String,
    ForeignKey,
    DateTime,
    text,
    Enum,
)
from sqlalchemy.dialects.postgresql import ENUM, JSONB
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from fastapi_utils.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL
from .database import Base


class User(Base):
    __tablename__ = "users"

    uuid = Column(
        GUID,
        primary_key=True,
        server_default=GUID_SERVER_DEFAULT_POSTGRESQL,
        nullable=False,
    )
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    email = Column(String, unique=True)
    phoneNumber = Column(String, unique=True)
    passwordHash = Column(String)
    resetPasswordToken = Column(String)
    resetPasswordExpires = Column(String)
    isVerified = Column(Boolean)
    bio = Column(String)
    country = Column(String)
    profilePicture = Column(String)
    dob = Column(DateTime)
    userName = Column(String, unique=True, nullable=False)
    online = Column(Boolean)
    role = Column(ENUM("ADMIN", "USER", name="role_enum"))
    isPrivate = Column(Boolean)
    createdAt = Column(
        TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False
    )


class Post(Base):
    __tablename__ = "post"

    uuid = Column(
        GUID,
        primary_key=True,
        server_default=GUID_SERVER_DEFAULT_POSTGRESQL,
        nullable=False,
    )
    postText = Column(String)
    previewText = Column(String)
    postedAt = Column(
        TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False
    )
    mediaLinks = Column(String)
    likeCount = Column(Integer)
    posterId = Column(
        Integer, ForeignKey("users.uuid", ondelete="CASCADE"), nullable=False
    )
    commentCount = Column(Integer)
    repostCount = Column(Integer)
    postType = Column(
        ENUM("POST", "REPOST", "STORY", "AD", name="role_enum"), nullable=False
    )
    reshared = Column(Boolean)
    reported = Column(Boolean)
    mentionList = Column(JSONB)

    postOwner = relationship("User")


class Like(Base):
    __tablename__ = "likes"

    uuid = Column(
        GUID,
        primary_key=True,
        server_default=GUID_SERVER_DEFAULT_POSTGRESQL,
        nullable=False,
    )
    userId = Column(Integer, ForeignKey("users.uuid", ondelete="CASCADE"))
    postId = Column(Integer, ForeignKey("post.uuid", ondelete="CASCADE"))


class Follower(Base):
    __tablename__ = "follower"

    uuid = Column(
        GUID,
        primary_key=True,
        server_default=GUID_SERVER_DEFAULT_POSTGRESQL,
        nullable=False,
    )
    userId = Column(
        Integer, ForeignKey("users.uuid", ondelete="CASCADE"), nullable=False
    )
    followerId = Column(
        Integer, ForeignKey("users.uuid", ondelete="CASCADE"), nullable=False
    )
    status = Column(Enum("ACCEPT", "PENDING"))
