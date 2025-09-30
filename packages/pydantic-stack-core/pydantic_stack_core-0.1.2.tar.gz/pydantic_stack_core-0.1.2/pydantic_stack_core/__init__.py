"""
Pydantic Stack Core - Typed hierarchical composition for structured text generation.

This library enables building complex documents through nested, typed Pydantic models
that render to composite strings through recursive composition.

Core Pattern: NESTED TYPED COMPOSITION
=======================================
The power isn't in concatenating strings - it's in building typed document trees
where each node knows how to render itself and its children.

Key Components:
1. RenderablePiece - Base class that enables nesting typed models within each other
2. MetaStack - Top-level container for any RenderablePiece models
3. generate_output_from_metastack - Triggers recursive rendering through the tree

The Real Power: HIERARCHICAL COMPOSITION
=========================================
RenderablePiece models can contain other RenderablePiece models as typed fields,
creating arbitrarily deep document structures with full type safety and validation.

Example - Nested Typed Composition:
    ```python
    from pydantic_stack_core import RenderablePiece, MetaStack
    from typing import List
    
    # Level 1: Atomic piece
    class Author(RenderablePiece):
        name: str
        bio: str
        
        def render(self) -> str:
            return f"**{self.name}** - {self.bio}"
    
    # Level 2: Piece containing pieces
    class Section(RenderablePiece):
        title: str
        content: str
        code_examples: List['CodeExample']  # NESTED TYPED MODELS!
        
        def render(self) -> str:
            output = f"## {self.title}\\n{self.content}\\n"
            for example in self.code_examples:
                output += example.render()  # RECURSIVE RENDERING!
            return output
    
    # Level 3: Deep nesting
    class BlogPost(RenderablePiece):
        title: str
        author: Author  # NESTED TYPED MODEL!
        sections: List[Section]  # NESTED LIST OF TYPED MODELS!
        
        def render(self) -> str:
            output = f"# {self.title}\\n\\n"
            output += self.author.render() + "\\n\\n"
            for section in self.sections:
                output += section.render()  # CASCADE OF RENDERS!
            return output
    
    # Build complex document through typed composition
    post = BlogPost(
        title="My Post",
        author=Author(name="Isaac", bio="AI Developer"),
        sections=[Section(...), Section(...)]
    )
    
    # Triggers recursive rendering through entire tree
    output = post.render()
    ```

Benefits:
- Type Safety: Can't put wrong types in wrong places
- Validation: Pydantic validates at every nesting level
- Composition: Build complex from simple, reuse components
- Discoverability: IDE shows exactly what goes where
"""

from .core import RenderablePiece, MetaStack, generate_output_from_metastack

__version__ = "0.1.0"
__all__ = ["RenderablePiece", "MetaStack", "generate_output_from_metastack"]