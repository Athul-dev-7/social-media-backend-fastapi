from pydantic import BaseModel, EmailStr, Json
from datetime import date, datetime
from enum import Enum


class RoleEnum(str, Enum):
    ADMIN = "ADMIN"
    USER = "USER"


class UserBase(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    phoneNumber: str | None = None
    resetPasswordToken: str | None = None
    resetPasswordExpires: str | None = None
    isVerified: bool = False
    bio: str | None = None
    country: str | None = None
    profilePicture: str | None = None
    dob: date | None = None
    userName: str
    online: bool = False
    role: RoleEnum = RoleEnum.USER
    isPrivate: bool = False
    createdAt: datetime


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    uuid: int
    firstName: str
    lastName: str
    email: EmailStr
    phoneNumber: str | None = None
    isVerified: bool = False
    bio: str | None = None
    country: str | None = None
    profilePicture: str | None = None
    dob: date | None = None
    userName: str
    online: bool = False
    role: RoleEnum = RoleEnum.USER
    isPrivate: bool = False
    createdAt: datetime

    class Config:
        orm_mode = True


class PostEnum(str, Enum):
    POST = "POST"
    REPOST = "REPOST"
    STORY = "STORY"
    AD = "AD"


class PostBase(BaseModel):
    postText: str | None = None
    previewText: str | None = None
    postedAt: datetime
    mediaLinks: str | None = None
    likeCount: int = 0
    posterId: int
    commentCount: int = 0
    repostCount: int = 0
    postType: PostEnum = PostEnum.POST
    reshared: bool = False
    reported: bool = False
    mentionList: Json


class PostCreate(PostBase):
    pass


class PostResponse(BaseModel):
    uuid: int
    post: PostBase


class Like(BaseModel):
    userId: int
    postId: int


class StatusEnum(str, Enum):
    ACCEPT = "ACCEPT"
    PENDING = "PENDING"


class Follower(BaseModel):
    userId: int
    followerId: int
    status: StatusEnum.PENDING | None = None
