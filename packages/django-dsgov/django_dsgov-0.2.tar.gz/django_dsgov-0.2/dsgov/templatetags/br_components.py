from django import template
from django.utils.html import format_html
from django.templatetags.static import static
from django.template.loader import render_to_string
from ..utils import build_page_url

register = template.Library()

@register.simple_tag
def br_stylesheets():
    """
    Renderiza as folhas de estilo principais do DSGov.
    Inclui o CSS do DSGov e a fonte Rawline.
    Os caminhos são resolvidos via staticfiles do Django.
    """
    return format_html(
        """
        <link rel="stylesheet" href="{}">
        <link rel="stylesheet" href="{}">
        """,
        static('dsgov/dist/css/styles.css'),
        static('dsgov/fonts/rawline/css/rawline.css')
    )


@register.simple_tag
def br_scripts():
    """
    Renderiza o script principal do DSGov.
    Inclui o bundle JS como módulo, necessário para componentes interativos.
    """
    return format_html(
        """
        <script type="module" src="{}"></script>
        """, 
        static('dsgov/dist/js/bundle.js')
    )


@register.simple_tag
def br_button(text='', button_type='', style='', extra_classes='', icon_class=''):
    """
    Renderiza um botão DSGov customizado.
    Permite definir texto, tipo, estilo (primary/secondary), classes extras e ícone.
    Os valores default garantem aparência consistente, mas podem ser sobrescritos no template.
    """
    style_class = f'{style}' if style in ['primary', 'secondary'] else ''
    classes = f'br-button {style_class} {extra_classes}'.strip()
    icon_html = format_html('<i class="{}" aria-hidden="true"></i>', icon_class) if icon_class else ''
    return format_html('<button type="{}" class="{}">{}{}</button>', button_type, classes, icon_html, text)


@register.simple_tag
def br_tag(tag_text="", tag_id="", icon_class="", close_button="", close_icon_class="", button_extra_classes="", extra_classes="", density=""):
    """
    Renderiza um componente de tag DSGov.
    Permite adicionar ícone, botão de fechar, classes extras e densidade.
    Os valores default garantem visual padrão, mas podem ser editados no template.
    """
    icon_html = format_html('<i class="{}" aria-hidden="true"></i>', icon_class) if icon_class else ""
    close_button_html = ""
    if close_button:
        close_button_html = format_html(
            '<button class="br-button inverted circle {}" type="button" aria-label="Fechar" aria-describedby="{}" data-dismiss="{}">'
            '<i class="{}" aria-hidden="true"></i></button>',
            button_extra_classes, tag_id, tag_id, close_icon_class
        )
    interaction_class = "interaction" if close_button else ""
    tag_html = format_html(
        '<span class="br-tag {} {} {}" id="{}" aria-describedby="{}">'
        '{}<span>{}</span>{}</span>',
        extra_classes, density, interaction_class, tag_id, tag_id, icon_html, tag_text, close_button_html
    )
    return format_html('<div class="d-flex align-items-center flex-wrap gap-2">{}</div>', tag_html)


@register.simple_tag
def br_input(input_type="", placeholder="", label="", input_id="", help_text="" ,extra_classes="", density="" , icon_class="", disabled=False, readonly=False, value=""):
    """
    Renderiza um campo de input DSGov.
    Permite definir tipo, placeholder, label, ajuda, ícone, estado (disabled/readonly) e classes extras.
    Os valores default garantem visual e acessibilidade, mas podem ser sobrescritos no template.
    """
    density_class = density if density in ['small', 'large'] else 'medium'
    classes = f'br-input {density_class} {extra_classes}'.strip()
    disabled_attr = 'disabled' if disabled else ''
    readonly_attr = 'readonly' if readonly else ''
    label_html = format_html('<label for="{}">{}</label>', input_id, label) if label else ''
    help_text_html = format_html('<p>{}</p>', help_text) if help_text else ''
    if icon_class:
        input_html = format_html(
            '<div class="input-group">'
            '<div class="input-icon"><i class="{}" aria-hidden="true"></i></div>'
            '<input type="{}" id="{}" placeholder="{}" value="{}" class="{}" {} {}/>'
            '</div>',
            icon_class, input_type, input_id, placeholder, value, extra_classes, disabled_attr, readonly_attr
        )
    else:
        input_html = format_html(
            '<input type="{}" id="{}" placeholder="{}" value="{}" class="{}" {} {}/>',
            input_type, input_id, placeholder, value, extra_classes, disabled_attr, readonly_attr
        )
    return format_html(
        '<div class="{}">{label_html}{input_html}{help_text_html}</div>',
        classes, label_html=label_html, input_html=input_html, help_text_html=help_text_html
    )


@register.simple_tag
def br_list(title, items):
    """
    Renderiza uma lista DSGov a partir de um template.
    Recebe título e itens, permitindo personalização no template.
    """
    context = {
        "title": title,
        "items": items,
    }
    return render_to_string("dsgov/components/list.html", context)


@register.inclusion_tag("dsgov/components/breadcrumb.html")
def br_breadcrumb(items=None, current_title=""):
    """
    Renderiza o componente de breadcrumb DSGov a partir de um template.
    Uso no template:
        {% br_breadcrumb items=breadcrumb_list current_title=page.title %}
    """
    return {
        "items": items or [],
        "current_title": current_title,
    }


@register.simple_tag(takes_context=True)
def br_pagination(context, total_pages=None, current_page=None, extra_params=""):
    """
    Renderiza paginação DSGov.

    - Funciona em Django puro e Django + Wagtail.
    - Recebe `total_pages` e `current_page` do contexto.
    - Mantém parâmetros da URL e adiciona `extra_params` se houver.
    """
    request = context["request"]

    if not total_pages or not current_page:
        return render_to_string("dsgov/components/pagination.html", context.flatten())

    total_pages = int(total_pages)
    current_page = int(current_page)

    # links prev/next
    prev_disabled = "disabled" if current_page <= 1 else ""
    next_disabled = "disabled" if current_page >= total_pages else ""
    prev_link = build_page_url(request, current_page - 1, extra_params) if current_page > 1 else "javascript:void(0)"
    next_link = build_page_url(request, current_page + 1, extra_params) if current_page < total_pages else "javascript:void(0)"

    def page_link(num, active=False):
        active_class = "active" if active else ""
        url = build_page_url(request, num, extra_params)
        return f"""
            <li>
              <a class="page {active_class}" href="{url}" aria-label="Página {num}">{num}</a>
            </li>
        """

    def ellipsis_block(start, end):
        items = "".join(
            f'<a class="br-item" href="{build_page_url(request, n, extra_params)}" role="menuitem">{n}</a>'
            for n in range(start, end + 1)
        )
        return f"""
            <li class="pagination-ellipsis">
              <button class="br-button circle" type="button" data-toggle="dropdown" aria-label="Abrir ou fechar a lista de paginação">
                <i class="fas fa-ellipsis-h" aria-hidden="true"></i>
              </button>
              <div class="br-list" role="menu">
                {items}
              </div>
            </li>
        """

    # Constrói números de página
    pages_html = page_link(1, active=(current_page == 1))

    if total_pages <= 7:
        for num in range(2, total_pages + 1):
            pages_html += page_link(num, active=(current_page == num))
    else:
        if current_page <= 4:
            for num in range(2, 6):
                pages_html += page_link(num, active=(current_page == num))
            if total_pages > 6:
                pages_html += ellipsis_block(6, total_pages - 1)
        elif current_page >= total_pages - 3:
            if total_pages > 6:
                pages_html += ellipsis_block(2, total_pages - 5)
            for num in range(total_pages - 4, total_pages):
                pages_html += page_link(num, active=(current_page == num))
        else:
            pages_html += ellipsis_block(2, current_page - 2)
            for num in range(current_page - 1, current_page + 2):
                pages_html += page_link(num, active=(current_page == num))
            pages_html += ellipsis_block(current_page + 2, total_pages - 1)

    # Adiciona a última página somente se ainda não estiver incluída
    if total_pages > 1 and (pages_html.find(f'aria-label="Página {total_pages}"') == -1):
        pages_html += page_link(total_pages, active=(current_page == total_pages))

    return format_html(
        """
        <nav class="br-pagination d-none d-sm-flex" aria-label="paginação" data-total="{total}" data-current="{current}">
          <ul>
            <li>
              <a class="br-button circle {prev_disabled}" href="{prev_link}" aria-label="Voltar página">
                <i class="fas fa-angle-left" aria-hidden="true"></i>
              </a>
            </li>
            {pages}
            <li>
              <a class="br-button circle {next_disabled}" href="{next_link}" aria-label="Página seguinte">
                <i class="fas fa-angle-right" aria-hidden="true"></i>
              </a>
            </li>
          </ul>
        </nav>
        """,
        total=total_pages,
        current=current_page,
        prev_disabled=prev_disabled,
        next_disabled=next_disabled,
        prev_link=prev_link,
        next_link=next_link,
        pages=format_html(pages_html),
    )


@register.simple_tag(takes_context=True)
def br_search(context, placeholder="Buscar...", input_id="search-input", btn_label="Buscar", input_name="q"):
    """
    Renderiza um campo de busca com botão.
    Agora preenche automaticamente com o valor digitado.
    Os valores default garantem funcionamento básico, mas podem ser sobrescritos no template.
    """
    request = context['request']
    value = request.GET.get(input_name, '')
    return format_html(
        """
        <form method="get" action="" class="mb-5">
            <div class="br-input input-highlight w-100">
                <label class="sr-only" for="{id}">Label / Rótulo</label>
                <input id="{id}" name="{name}" type="search" placeholder="{ph}" value="{val}" class="w-100">
                <button class="br-button" type="submit" aria-label="{btn}">
                <i class="fas fa-search" aria-hidden="true"></i>
                </button>
            </div>
        </form>
        """,
        id=input_id,
        ph=placeholder,
        btn=btn_label,
        name=input_name,
        val=value
    )


@register.simple_tag
def br_card(title='', text='', icon_class=None, icon_extra_class="", icon_style="", title_class="mt-0 mb-1 text-primary", title_style="font-family: 'Noto Sans', sans-serif;", text_class="text-gray-700", text_style="font-family: 'Noto Sans', sans-serif; color:#5C5C5C;"):
    """
    Renderiza um card customizado com ícone, título e texto, seguindo o padrão visual do DSGov.
    Os parâmetros permitem personalizar classes e estilos do card diretamente pelo template.

    Os valores default dos parâmetros garantem que o card tenha estilos, cores e espaçamentos padronizados,
    mesmo que nenhum valor seja passado pelo template. Isso facilita o uso rápido e mantém a identidade visual.

    Mesmo com esses valores padrão, é possível sobrescrever qualquer parâmetro manualmente no template,
    permitindo total controle sobre o visual do card conforme a necessidade do projeto.
    """
    context = {
        "title": title,
        "text": text,
        "icon_class": icon_class,
        "icon_extra_class": icon_extra_class,
        "icon_style": icon_style,
        "title_class": title_class,
        "title_style": title_style,
        "text_class": text_class,
        "text_style": text_style,
    }
    return render_to_string("dsgov/components/card_with_icon.html", context)
