"""
Document admin interfaces using Django Admin Utilities.

Enhanced document management with Material Icons and optimized queries.
"""

from django.contrib import admin, messages
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.db import models, IntegrityError
from django.db.models import Count, Sum, Avg, Q
from django.db.models.fields.json import JSONField
from django_json_widget.widgets import JSONEditorWidget
from unfold.admin import ModelAdmin, TabularInline
from unfold.contrib.filters.admin import AutocompleteSelectFilter, AutocompleteSelectMultipleFilter
from unfold.contrib.forms.widgets import WysiwygWidget
from django_cfg import ImportExportModelAdmin, ExportMixin, ImportForm, ExportForm

from django_cfg.modules.django_admin import (
    OptimizedModelAdmin,
    DisplayMixin,
    MoneyDisplayConfig,
    StatusBadgeConfig,
    DateTimeDisplayConfig,
    Icons,
    ActionVariant,
    display,
    action
)
from django_cfg.modules.django_admin.utils.badges import StatusBadge

from ..models import Document, DocumentChunk, DocumentCategory


class DocumentChunkInline(TabularInline):
    """Inline for document chunks with Unfold styling."""
    
    model = DocumentChunk
    verbose_name = "Document Chunk"
    verbose_name_plural = "📄 Document Chunks (Read-only)"
    extra = 0
    max_num = 0
    can_delete = False
    show_change_link = True
    
    def has_add_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    fields = [
        'short_uuid', 'chunk_index', 'content_preview_inline', 'token_count', 
        'has_embedding_inline', 'embedding_cost'
    ]
    readonly_fields = [
        'short_uuid', 'chunk_index', 'content_preview_inline', 'token_count', 'character_count',
        'has_embedding_inline', 'embedding_cost', 'created_at'
    ]
    
    hide_title = False
    classes = ['collapse']
    
    @display(description="Content Preview")
    def content_preview_inline(self, obj):
        """Shortened content preview for inline display."""
        if not obj.content:
            return "—"
        return obj.content[:100] + "..." if len(obj.content) > 100 else obj.content
    
    @display(description="Has Embedding", boolean=True)
    def has_embedding_inline(self, obj):
        """Check if chunk has embedding vector for inline."""
        return obj.embedding is not None and len(obj.embedding) > 0
    
    def get_queryset(self, request):
        """Optimize queryset for inline display."""
        return super().get_queryset(request).select_related('document', 'user')


@admin.register(Document)
class DocumentAdmin(OptimizedModelAdmin, DisplayMixin, ModelAdmin, ImportExportModelAdmin):
    """Admin interface for Document model using Django Admin Utilities."""
    
    # Performance optimization
    select_related_fields = ['user']
    
    # Import/Export configuration
    import_form_class = ImportForm
    export_form_class = ExportForm
    
    list_display = [
        'title_display', 'categories_display', 'user_display', 
        'visibility_display', 'status_display', 'chunks_count_display', 
        'vectorization_progress', 'tokens_display', 'cost_display', 'created_at_display'
    ]
    list_display_links = ['title_display']
    ordering = ['-created_at']
    inlines = [DocumentChunkInline]
    list_filter = [
        'processing_status', 'is_public', 'file_type', 'created_at',
        ('user', AutocompleteSelectFilter),
        ('categories', AutocompleteSelectMultipleFilter)
    ]
    search_fields = ['title', 'user__username', 'user__email']
    autocomplete_fields = ['user', 'categories']
    readonly_fields = [
        'id', 'user', 'content_hash', 'file_size', 'processing_started_at',
        'processing_completed_at', 'chunks_count', 'total_tokens',
        'processing_error', 'processing_duration', 'processing_status',
        'total_cost_usd', 'created_at', 'updated_at', 'duplicate_check'
    ]
    
    fieldsets = (
        ('📄 Basic Information', {
            'fields': ('id', 'title', 'user', 'categories', 'is_public', 'file_type', 'file_size'),
            'classes': ('tab',)
        }),
        ('📝 Content', {
            'fields': ('content', 'content_hash', 'duplicate_check'),
            'classes': ('tab',)
        }),
        ('⚙️ Processing Status', {
            'fields': (
                'processing_status', 'processing_started_at', 
                'processing_completed_at', 'processing_error'
            ),
            'classes': ('tab',)
        }),
        ('📊 Statistics', {
            'fields': ('chunks_count', 'total_tokens', 'total_cost_usd'),
            'classes': ('tab',)
        }),
        ('🔧 Metadata', {
            'fields': ('metadata',),
            'classes': ('tab', 'collapse'),
            'description': 'Auto-generated metadata (read-only)'
        }),
        ('⏰ Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('tab', 'collapse')
        })
    )
    filter_horizontal = ['categories']
    
    # Unfold configuration
    compressed_fields = True
    warn_unsaved_form = True
    
    # Form field overrides
    formfield_overrides = {
        models.TextField: {"widget": WysiwygWidget},
        JSONField: {"widget": JSONEditorWidget}
    }
    
    actions = ['reprocess_documents', 'mark_as_public', 'mark_as_private']
    
    def get_queryset(self, request):
        """Optimize queryset with select_related and prefetch_related."""
        queryset = Document.objects.all_users().select_related('user').prefetch_related('categories')
        
        if not request.user.is_superuser:
            queryset = queryset.filter(user=request.user)
        
        return queryset
    
    def save_model(self, request, obj, form, change):
        """Automatically set user to current user when creating new documents."""
        if not change:
            obj.user = request.user
            
            is_duplicate, existing_doc = Document.objects.check_duplicate_before_save(
                user=obj.user, 
                content=obj.content
            )
            
            if is_duplicate and existing_doc:
                messages.error(
                    request,
                    f'❌ A document with identical content already exists: "{existing_doc.title}" '
                    f'(created {existing_doc.created_at.strftime("%Y-%m-%d %H:%M")}). '
                    f'Please modify the content or update the existing document.'
                )
                return
        
        try:
            super().save_model(request, obj, form, change)
        except IntegrityError as e:
            if 'unique_user_document' in str(e):
                messages.error(
                    request,
                    'A document with identical content already exists for this user. '
                    'Please modify the content or update the existing document.'
                )
            else:
                messages.error(request, f'Database error: {str(e)}')
            raise
    
    @display(description="Document Title", ordering="title")
    def title_display(self, obj):
        """Display document title with truncation."""
        title = obj.title or "Untitled Document"
        if len(title) > 50:
            title = title[:47] + "..."
        
        config = StatusBadgeConfig(show_icons=True, icon=Icons.DESCRIPTION)
        return StatusBadge.create(
            text=title,
            variant="primary",
            config=config
        )
    
    @display(description="User")
    def user_display(self, obj):
        """User display."""
        if not obj.user:
            return "—"
        return self.display_user_simple(obj.user)
    
    @display(description="Visibility")
    def visibility_display(self, obj):
        """Display visibility status."""
        if obj.is_public:
            config = StatusBadgeConfig(show_icons=True, icon=Icons.PUBLIC)
            return StatusBadge.create(text="Public", variant="success", config=config)
        else:
            config = StatusBadgeConfig(show_icons=True, icon=Icons.LOCK)
            return StatusBadge.create(text="Private", variant="danger", config=config)
    
    @display(description="Status")
    def status_display(self, obj):
        """Display processing status."""
        status_config = StatusBadgeConfig(
            custom_mappings={
                'pending': 'warning',
                'processing': 'info',
                'completed': 'success',
                'failed': 'danger',
                'cancelled': 'secondary'
            },
            show_icons=True,
            icon=Icons.CHECK_CIRCLE if obj.processing_status == 'completed' else Icons.ERROR if obj.processing_status == 'failed' else Icons.SCHEDULE
        )
        return self.display_status_auto(obj, 'processing_status', status_config)
    
    @display(description="Categories")
    def categories_display(self, obj):
        """Display categories count."""
        categories = obj.categories.all()
        
        if not categories:
            return "No categories"
        
        public_count = sum(1 for cat in categories if cat.is_public)
        private_count = len(categories) - public_count
        
        if private_count == 0:
            return f"{len(categories)} public"
        elif public_count == 0:
            return f"{len(categories)} private"
        else:
            return f"{public_count} public, {private_count} private"
    
    @display(description="Chunks", ordering="chunks_count")
    def chunks_count_display(self, obj):
        """Display chunks count."""
        count = obj.chunks_count
        if count > 0:
            return f"{count} chunks"
        return "0 chunks"
    
    @display(description="Tokens", ordering="total_tokens")
    def tokens_display(self, obj):
        """Display token count with formatting."""
        tokens = obj.total_tokens
        if tokens > 1000:
            return f"{tokens/1000:.1f}K"
        return str(tokens)

    @display(description="Cost (USD)", ordering="total_cost_usd")
    def cost_display(self, obj):
        """Display cost with currency formatting."""
        config = MoneyDisplayConfig(
            currency="USD",
            decimal_places=6,
            show_sign=False
        )
        return self.display_money_amount(obj, 'total_cost_usd', config)
    
    @display(description="Vectorization")
    def vectorization_progress(self, obj):
        """Display vectorization progress."""
        return Document.objects.get_vectorization_status_display(obj)
    
    @display(description="Created")
    def created_at_display(self, obj):
        """Created time with relative display."""
        config = DateTimeDisplayConfig(show_relative=True)
        return self.display_datetime_relative(obj, 'created_at', config)
    
    @display(description="Processing Duration")
    def processing_duration_display(self, obj):
        """Display processing duration in readable format."""
        duration = obj.processing_duration
        if duration is None:
            return "N/A"
        
        if duration < 60:
            return f"{duration:.1f}s"
        elif duration < 3600:
            minutes = duration / 60
            return f"{minutes:.1f}m"
        else:
            hours = duration / 3600
            return f"{hours:.1f}h"
    
    @display(description="Duplicate Check")
    def duplicate_check(self, obj):
        """Check for duplicate documents with same content."""
        duplicate_info = Document.objects.get_duplicate_info(obj)
        
        if isinstance(duplicate_info, str):
            if "No duplicates found" in duplicate_info:
                return "✓ No duplicates found"
            return duplicate_info
        
        duplicates_data = duplicate_info['duplicates']
        count = duplicate_info['count']
        
        duplicate_names = [dup.title for dup in duplicates_data[:3]]
        result = f"⚠️ Found {count} duplicate(s): " + ", ".join(duplicate_names)
        if count > 3:
            result += f" and {count - 3} more"
        
        return result
    
    @action(description="Reprocess documents", variant=ActionVariant.INFO)
    def reprocess_documents(self, request, queryset):
        """Reprocess selected documents."""
        count = queryset.count()
        messages.info(request, f"Reprocessing functionality not implemented yet. {count} documents selected.")
    
    @action(description="Mark as public", variant=ActionVariant.SUCCESS)
    def mark_as_public(self, request, queryset):
        """Mark selected documents as public."""
        updated = queryset.update(is_public=True)
        messages.success(request, f"Marked {updated} documents as public.")
    
    @action(description="Mark as private", variant=ActionVariant.WARNING)
    def mark_as_private(self, request, queryset):
        """Mark selected documents as private."""
        updated = queryset.update(is_public=False)
        messages.warning(request, f"Marked {updated} documents as private.")
    
    def changelist_view(self, request, extra_context=None):
        """Add summary statistics to changelist."""
        extra_context = extra_context or {}
        
        queryset = self.get_queryset(request)
        stats = queryset.aggregate(
            total_documents=Count('id'),
            total_chunks=Sum('chunks_count'),
            total_tokens=Sum('total_tokens'),
            total_cost=Sum('total_cost_usd')
        )
        
        status_counts = dict(
            queryset.values_list('processing_status').annotate(
                count=Count('id')
            )
        )
        
        extra_context['summary_stats'] = {
            'total_documents': stats['total_documents'] or 0,
            'total_chunks': stats['total_chunks'] or 0,
            'total_tokens': stats['total_tokens'] or 0,
            'total_cost': f"${(stats['total_cost'] or 0):.6f}",
            'status_counts': status_counts
        }
        
        return super().changelist_view(request, extra_context)


@admin.register(DocumentChunk)
class DocumentChunkAdmin(OptimizedModelAdmin, DisplayMixin, ModelAdmin):
    """Admin interface for DocumentChunk model using Django Admin Utilities."""
    
    # Performance optimization
    select_related_fields = ['document', 'user']
    
    list_display = [
        'chunk_display', 'document_display', 'user_display', 'token_count_display', 
        'embedding_status', 'embedding_cost_display', 'created_at_display'
    ]
    list_display_links = ['chunk_display']
    ordering = ['-created_at']
    list_filter = [
        'embedding_model', 'created_at',
        ('user', AutocompleteSelectFilter),
        ('document', AutocompleteSelectFilter)
    ]
    search_fields = ['document__title', 'user__username', 'content']
    readonly_fields = [
        'id', 'embedding_info', 'token_count', 'character_count',
        'embedding_cost', 'created_at', 'updated_at', 'content_preview'
    ]
    
    fieldsets = (
        ('📄 Basic Information', {
            'fields': ('id', 'document', 'user', 'chunk_index'),
            'classes': ('tab',)
        }),
        ('📝 Content', {
            'fields': ('content_preview', 'content'),
            'classes': ('tab',)
        }),
        ('🔗 Embedding Information', {
            'fields': ('embedding_model', 'token_count', 'character_count', 'embedding_cost'),
            'classes': ('tab',)
        }),
        ('🧠 Vector Embedding', {
            'fields': ('embedding',),
            'classes': ('tab', 'collapse')
        }),
        ('🔧 Metadata', {
            'fields': ('metadata',),
            'classes': ('tab', 'collapse'),
            'description': 'Auto-generated chunk metadata (read-only)'
        }),
        ('⏰ Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('tab', 'collapse')
        })
    )
    
    # Unfold configuration
    compressed_fields = True
    warn_unsaved_form = True
    
    # Form field overrides
    formfield_overrides = {
        JSONField: {"widget": JSONEditorWidget}
    }
    
    actions = ['regenerate_embeddings', 'clear_embeddings']
    
    @display(description="Chunk", ordering="chunk_index")
    def chunk_display(self, obj):
        """Display chunk identifier."""
        config = StatusBadgeConfig(show_icons=True, icon=Icons.ARTICLE)
        return StatusBadge.create(
            text=f"Chunk {obj.chunk_index + 1}",
            variant="info",
            config=config
        )
    
    @display(description="Document", ordering="document__title")
    def document_display(self, obj):
        """Display document title."""
        return obj.document.title
    
    @display(description="User")
    def user_display(self, obj):
        """User display."""
        if not obj.user:
            return "—"
        return self.display_user_simple(obj.user)
    
    @display(description="Tokens", ordering="token_count")
    def token_count_display(self, obj):
        """Display token count with formatting."""
        tokens = obj.token_count
        if tokens > 1000:
            return f"{tokens/1000:.1f}K"
        return str(tokens)
    
    @display(description="Embedding")
    def embedding_status(self, obj):
        """Display embedding status."""
        has_embedding = obj.embedding is not None and len(obj.embedding) > 0
        if has_embedding:
            config = StatusBadgeConfig(show_icons=True, icon=Icons.CHECK_CIRCLE)
            return StatusBadge.create(text="✓ Vectorized", variant="success", config=config)
        else:
            config = StatusBadgeConfig(show_icons=True, icon=Icons.ERROR)
            return StatusBadge.create(text="✗ Not vectorized", variant="danger", config=config)
    
    @display(description="Cost (USD)", ordering="embedding_cost")
    def embedding_cost_display(self, obj):
        """Display embedding cost with currency formatting."""
        config = MoneyDisplayConfig(
            currency="USD",
            decimal_places=6,
            show_sign=False
        )
        return self.display_money_amount(obj, 'embedding_cost', config)
    
    @display(description="Created")
    def created_at_display(self, obj):
        """Created time with relative display."""
        config = DateTimeDisplayConfig(show_relative=True)
        return self.display_datetime_relative(obj, 'created_at', config)
    
    @display(description="Content Preview")
    def content_preview(self, obj):
        """Display content preview with truncation."""
        return obj.content[:200] + "..." if len(obj.content) > 200 else obj.content
    
    @display(description="Embedding Info")
    def embedding_info(self, obj):
        """Display embedding information safely."""
        if obj.embedding is not None and len(obj.embedding) > 0:
            return f"✓ Vector ({len(obj.embedding)} dimensions)"
        return "✗ No embedding"
    
    @action(description="Regenerate embeddings", variant=ActionVariant.INFO)
    def regenerate_embeddings(self, request, queryset):
        """Regenerate embeddings for selected chunks."""
        count = queryset.count()
        messages.info(request, f"Regenerate embeddings functionality not implemented yet. {count} chunks selected.")
    
    @action(description="Clear embeddings", variant=ActionVariant.WARNING)
    def clear_embeddings(self, request, queryset):
        """Clear embeddings for selected chunks."""
        updated = queryset.update(embedding=None)
        messages.warning(request, f"Cleared embeddings for {updated} chunks.")
    
    def changelist_view(self, request, extra_context=None):
        """Add chunk statistics to changelist."""
        extra_context = extra_context or {}
        
        queryset = self.get_queryset(request)
        stats = queryset.aggregate(
            total_chunks=Count('id'),
            total_tokens=Sum('token_count'),
            total_characters=Sum('character_count'),
            total_embedding_cost=Sum('embedding_cost'),
            avg_tokens_per_chunk=Avg('token_count')
        )
        
        model_counts = dict(
            queryset.values_list('embedding_model').annotate(
                count=Count('id')
            )
        )
        
        extra_context['chunk_stats'] = {
            'total_chunks': stats['total_chunks'] or 0,
            'total_tokens': stats['total_tokens'] or 0,
            'total_characters': stats['total_characters'] or 0,
            'total_embedding_cost': f"${(stats['total_embedding_cost'] or 0):.6f}",
            'avg_tokens_per_chunk': f"{(stats['avg_tokens_per_chunk'] or 0):.0f}",
            'model_counts': model_counts
        }
        
        return super().changelist_view(request, extra_context)


@admin.register(DocumentCategory)
class DocumentCategoryAdmin(OptimizedModelAdmin, DisplayMixin, ModelAdmin, ImportExportModelAdmin):
    """Admin interface for DocumentCategory model using Django Admin Utilities."""
    
    # Import/Export configuration
    import_form_class = ImportForm
    export_form_class = ExportForm
    
    list_display = [
        'short_uuid', 'name_display', 'visibility_display', 'document_count', 'created_at_display'
    ]
    list_display_links = ['name_display']
    ordering = ['-created_at']
    list_filter = ['is_public', 'created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['id', 'created_at', 'updated_at']
    
    fieldsets = (
        ('📁 Basic Information', {
            'fields': ('id', 'name', 'description', 'is_public'),
            'classes': ('tab',)
        }),
        ('⏰ Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('tab', 'collapse')
        })
    )
    
    # Unfold configuration
    compressed_fields = True
    warn_unsaved_form = True
    
    # Form field overrides
    formfield_overrides = {
        models.TextField: {"widget": WysiwygWidget}
    }
    
    actions = ['make_public', 'make_private']
    
    @display(description="Category Name")
    def name_display(self, obj):
        """Display category name."""
        config = StatusBadgeConfig(show_icons=True, icon=Icons.FOLDER)
        return StatusBadge.create(
            text=obj.name,
            variant="primary",
            config=config
        )
    
    @display(description="Visibility")
    def visibility_display(self, obj):
        """Display visibility status."""
        if obj.is_public:
            config = StatusBadgeConfig(show_icons=True, icon=Icons.PUBLIC)
            return StatusBadge.create(text="Public", variant="success", config=config)
        else:
            config = StatusBadgeConfig(show_icons=True, icon=Icons.LOCK)
            return StatusBadge.create(text="Private", variant="danger", config=config)
    
    @display(description="Documents", ordering="document_count")
    def document_count(self, obj):
        """Display count of documents in this category."""
        count = obj.documents.count()
        return f"{count} documents"
    
    @display(description="Created")
    def created_at_display(self, obj):
        """Created time with relative display."""
        config = DateTimeDisplayConfig(show_relative=True)
        return self.display_datetime_relative(obj, 'created_at', config)
    
    @action(description="Make public", variant=ActionVariant.SUCCESS)
    def make_public(self, request, queryset):
        """Make selected categories public."""
        updated = queryset.update(is_public=True)
        messages.success(request, f"Made {updated} categories public.")
    
    @action(description="Make private", variant=ActionVariant.WARNING)
    def make_private(self, request, queryset):
        """Make selected categories private."""
        updated = queryset.update(is_public=False)
        messages.warning(request, f"Made {updated} categories private.")
    
    def get_queryset(self, request):
        """Optimize queryset with prefetch_related."""
        return super().get_queryset(request).prefetch_related('documents')
    
    def changelist_view(self, request, extra_context=None):
        """Add category statistics to changelist."""
        extra_context = extra_context or {}
        
        queryset = self.get_queryset(request)
        stats = queryset.aggregate(
            total_categories=Count('id'),
            public_categories=Count('id', filter=models.Q(is_public=True)),
            private_categories=Count('id', filter=models.Q(is_public=False))
        )
        
        extra_context['category_stats'] = {
            'total_categories': stats['total_categories'] or 0,
            'public_categories': stats['public_categories'] or 0,
            'private_categories': stats['private_categories'] or 0
        }
        
        return super().changelist_view(request, extra_context)
