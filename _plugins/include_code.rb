module Jekyll
  class IncludeCode < Liquid::Tag
    SYNTAX = /(#{Liquid::QuotedString}+)(\s+lang=(\w+))?(\s+lines=(\d+-\d+))?/o
    
    def initialize(tag_name, markup, tokens)
      super
      match = markup.strip.match(SYNTAX)
      raise SyntaxError, "IncludeCode 语法错误" unless match

      @path = match[1].gsub(/(^['"]|['"]$)/, '')
      @lang = match[3] || File.extname(@path).delete('.')
      @lines = match[5]
    end

def render(context)
  site = context.registers[:site]
  base_path = File.realpath(site.source) # 获取项目绝对路径
  
  # 校验路径是否在项目目录内
  full_path = File.expand_path(@path, base_path)
  unless full_path.start_with?(base_path)
    raise SecurityError, "禁止访问项目目录外的文件: #{@path}"
  end
    

      # 读取文件内容
      content = File.read(full_path)
      
      # 行号处理
      if @lines
        start, finish = @lines.split('-').map(&:to_i)
        content = content.lines[start-1..finish-1].join
      end

      # 生成带高亮的代码块
      <<~HTML
        <div class="code-snippet" data-lang="#{@lang}">
          <pre><code class="language-#{@lang}">#{CGI.escapeHTML(content)}</code></pre>
          <div class="file-path">#{@path}</div>
        </div>
      HTML
    end
  end
end

Liquid::Template.register_tag('include_code', Jekyll::IncludeCode)
