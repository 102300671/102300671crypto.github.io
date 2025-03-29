module Jekyll
  class IncludeCode < Liquid::Tag
    SYNTAX = %r!^(\S+)(?:\s+lang=(\w+))?(?:\s+lines=(\d+-\d+))?$!
    # _plugins/include_code.rb
    DEFAULT_ALLOWED_PATHS = %w[nssctf/一 nssctf/二 assets/attachments/].freeze

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
      normalized_path = normalize_path(@raw_path, base_path)
      full_path = build_full_path(normalized_path, base_path)

      validate_path(full_path, normalized_path, base_path)
      content = process_content(full_path)
      generate_html(content, normalized_path, site)
    end

    private

    def normalize_path(raw_path, base_path)
      File.expand_path(raw_path, base_path)
    end

    def build_full_path(normalized_path, _base_path)
      normalized_path
    end

    def validate_path(full_path, normalized_path, base_path)
      allowed_paths = DEFAULT_ALLOWED_PATHS.map { |allowed| File.expand_path(allowed, base_path) }
      unless full_path.start_with?(base_path) && allowed_paths.any? { |allowed| full_path.start_with?(allowed) }
        raise SecurityError, "Access to the path '#{normalized_path}' is not allowed."
      end
    end

    def process_content(full_path)
      raise IOError, "File not found: #{full_path}" unless File.exist?(full_path)

      content = File.read(full_path)
      if @lines
        start_line, end_line = @lines.split('-').map(&:to_i)
        content = content.lines[start_line - 1..end_line - 1].join
      end
      content
    end

    def generate_html(content, path, context)
      <<~HTML
        <div class="code-snippet">
          <div class="code-header">
            <span class="file-name">#{File.basename(path)}</span>
          </div>
          <pre><code class="language-#{@lang}">#{content}</code></pre>
        </div>
      HTML
    end
  end
end

Liquid::Template.register_tag('include_code', Jekyll::IncludeCode)