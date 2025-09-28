"""
Tag utilities for OpenWrite.
Handles tag parsing, creation, and management operations.
"""

import re
from typing import List, Set, Tuple, Optional
from sqlalchemy.orm import Session
from .models import Tag, PostTag, Post


def normalize_tag(tag: str) -> str:
    """
    Normalize a tag name by removing special characters and converting to lowercase.
    
    Args:
        tag: Raw tag string (e.g., "#Music", "  games  ", "web-dev")
    
    Returns:
        Normalized tag name (e.g., "music", "games", "web-dev")
    """
    # Remove leading/trailing whitespace and # symbols
    tag = tag.strip().lstrip('#')
    
    # Convert to lowercase
    tag = tag.lower()
    
    # Only allow alphanumeric characters, hyphens, and underscores
    tag = re.sub(r'[^a-z0-9\-_]', '', tag)
    
    # Remove multiple consecutive hyphens/underscores
    tag = re.sub(r'[-_]+', '-', tag)
    
    # Remove leading/trailing hyphens/underscores
    tag = tag.strip('-_')
    
    return tag


def parse_tags_from_input(tags_input: str) -> List[str]:
    """
    Parse tags from user input string.
    
    Args:
        tags_input: Comma-separated tags (e.g., "#music, games, #web-dev")
    
    Returns:
        List of normalized tag names
    """
    if not tags_input or not tags_input.strip():
        return []
    
    # Split by comma and normalize each tag
    tags = []
    for tag in tags_input.split(','):
        normalized = normalize_tag(tag)
        if normalized and normalized not in tags:  # Avoid duplicates
            tags.append(normalized)
    
    return tags


def parse_tags_from_posts_syntax(posts_syntax: str) -> List[str]:
    """
    Parse tags from {posts:#tag1,#tag2} syntax.
    
    Args:
        posts_syntax: Posts template syntax (e.g., "{posts:#music,#games}")
    
    Returns:
        List of normalized tag names, empty list if no tags specified
    """
    # Match {posts}, {posts:}, {posts:#tag1}, {posts:#tag1,#tag2}
    match = re.match(r'\{posts(?::([^}]+))?\}', posts_syntax.strip())
    
    if not match or not match.group(1):
        return []
    
    tags_part = match.group(1)
    return parse_tags_from_input(tags_part)


def get_or_create_tag(db: Session, tag_name: str) -> Tag:
    """
    Get existing tag or create a new one.
    
    Args:
        db: Database session
        tag_name: Normalized tag name
    
    Returns:
        Tag model instance
    """
    tag = db.query(Tag).filter_by(name=tag_name).first()
    
    if not tag:
        tag = Tag(name=tag_name)
        db.add(tag)
        db.flush()  # Get the ID without committing
    
    return tag


def update_post_tags(db: Session, post: Post, tag_names: List[str]) -> None:
    """
    Update tags for a post.
    
    Args:
        db: Database session
        post: Post model instance
        tag_names: List of normalized tag names
    """
    # Remove existing tags for this post
    db.query(PostTag).filter_by(post_id=post.id).delete()
    
    # Add new tags
    for tag_name in tag_names:
        if tag_name:  # Skip empty tags
            tag = get_or_create_tag(db, tag_name)
            post_tag = PostTag(post_id=post.id, tag_id=tag.id)
            db.add(post_tag)


def get_post_tags(db: Session, post: Post) -> List[str]:
    """
    Get all tags for a post.
    
    Args:
        db: Database session
        post: Post model instance
    
    Returns:
        List of tag names
    """
    tags = db.query(Tag).join(PostTag).filter_by(post_id=post.id).all()
    return [tag.name for tag in tags]


def get_posts_by_tags(db: Session, blog_id: int, tag_names: List[str], limit: Optional[int] = None) -> List[Post]:
    """
    Get posts filtered by tags.
    
    Args:
        db: Database session
        blog_id: Blog ID to filter by
        tag_names: List of tag names to filter by
        limit: Optional limit on number of posts
    
    Returns:
        List of Post model instances
    """
    if not tag_names:
        # No tags specified, return all posts
        query = db.query(Post).filter_by(blog=blog_id).filter_by(isdraft='0').order_by(Post.id.desc())
    else:
        # Filter by tags
        query = (
            db.query(Post)
            .join(PostTag, Post.id == PostTag.post_id)
            .join(Tag, PostTag.tag_id == Tag.id)
            .filter(Post.blog == blog_id)
            .filter(Post.isdraft == '0')
            .filter(Tag.name.in_(tag_names))
            .distinct()
            .order_by(Post.id.desc())
        )
    
    if limit:
        query = query.limit(limit)
    
    return query.all()


def get_all_blog_tags(db: Session, blog_id: int) -> List[Tuple[str, int]]:
    """
    Get all tags used in a blog with their post counts.
    
    Args:
        db: Database session
        blog_id: Blog ID
    
    Returns:
        List of tuples (tag_name, post_count)
    """
    from sqlalchemy import func
    
    result = (
        db.query(Tag.name, func.count(PostTag.post_id).label('post_count'))
        .join(PostTag, Tag.id == PostTag.tag_id)
        .join(Post, PostTag.post_id == Post.id)
        .filter(Post.blog == blog_id)
        .filter(Post.isdraft == '0')
        .group_by(Tag.id, Tag.name)
        .order_by(func.count(PostTag.post_id).desc())
        .all()
    )
    
    return [(name, count) for name, count in result]


def search_tags(db: Session, query: str, limit: int = 10) -> List[str]:
    """
    Search for tags matching a query (for autocomplete).
    
    Args:
        db: Database session
        query: Search query
        limit: Maximum number of results
    
    Returns:
        List of matching tag names
    """
    normalized_query = normalize_tag(query)
    
    if not normalized_query:
        return []
    
    tags = (
        db.query(Tag)
        .filter(Tag.name.like(f'{normalized_query}%'))
        .order_by(Tag.name)
        .limit(limit)
        .all()
    )
    
    return [tag.name for tag in tags]


def format_tags_for_display(tag_names: List[str]) -> str:
    """
    Format tags for display in templates.
    
    Args:
        tag_names: List of tag names
    
    Returns:
        Formatted string for display
    """
    if not tag_names:
        return ""
    
    return ", ".join(f"#{tag}" for tag in tag_names)