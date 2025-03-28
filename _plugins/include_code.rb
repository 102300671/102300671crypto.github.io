module Jekyll
  class IncludeCode < Liquid::Tag
    SYNTAX = %r!^(\S+)(?:\s+lang=(\w+))?(?:\s+lines=(\d+-\d+))?$!
    DEFAULT_ALLOWED_PATHS = %w[nssctf/ assets/attachments/].freeze

    def initialize(tag_name, markup, tokens)
      super
      @match = markup.strip.match(SYNTAX)
      raise SyntaxError, "Invalid include_code syntax. Usage: {% include_code path [lang=xx] [lines=x-y] %}" unless @match

      @raw_path = @match[1].delete("'\"")
      @lang = @match[2] || File.extname(@raw_path).delete('.')
      @lines = @match[3]
    end

    def render(context)
      site = context.registers[:site]
      base_path = File.realpath(site.source)
      normalized_path = normalize_path(@raw_path)
      full_path = build_full_path(normalized_path, base_path)

      validate_path(full_path, normalized_path, base_path)
      content = process_content(full_path)
      generate_html(content, normalized_path, site)
    end

    private

    # 保留原有路径处理方法...
    
    def generate_html(content, path, context)
      highlighted_content = highlight_code(content, context)
      
      <<~HTML
        <div class="code-snippet" data-lang="#{@lang}">
          <div class="code-header">
            <span class="file-name">#{File.basename(path)}</span>
            <span class="copy-button" onclick="copyCode(this)">复制</span>
          </div>
          <pre><code class="language-#{@lang}">#{highlighted_content}</code></pre>
          <div class="file-path" title="#{path}">
            <svg class="octicon" aria-hidden="true" width="12" height="12">
              <use xlink:href="#file-icon" />
            </svg>
            #{truncate_path(path)}
          </div>
        </div>
        <script>
          function copyCode(btn) {
            const codeBlock = btn.parentNode.nextElementSibling.querySelector('code');
            const range = document.createRange();
            range.selectNode(codeBlock);
            window.getSelection().removeAllRanges();
            window.getSelection().addRange(range);
            document.execCommand('copy');
            btn.textContent = '已复制!';
            setTimeout(() => btn.textContent = '复制', 2000);
          }
        </script>
      HTML
    end

    # 保留其他方法...
  end
end

Liquid::Template.register_tag('include_code', Jekyll::IncludeCode)