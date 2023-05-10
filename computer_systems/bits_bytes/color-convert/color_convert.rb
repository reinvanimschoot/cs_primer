def parse_css_file(css)
  css.gsub(/\#([0-9a-fA-f]+)/) do |match|
    match.slice!(0)
    hex_to_rgb(match)
  end
end

def hex_to_rgb(hex_string)
  rgb_values = []

  xx_groups = xx_values(hex_string)

  xx_groups.each { |xx| rgb_values << xx_to_dec(xx) }

  rgb_string(rgb_values)
end

def xx_to_dec(xx)
  map = Hash[%i[0 1 2 3 4 5 6 7 8 9 a b c d e f].zip(0..16)]

  n1 = xx[0].downcase.to_sym
  n2 = xx[1].downcase.to_sym

  (map[n1] << 4) + map[n2]
end

def rgb_string(rgb_values)
  r, g, b, a = rgb_values

  label = a ? "rgba" : "rgb"

  string = "#{label}(#{r} #{g} #{b}"

  string += " #{a.to_f / 256}" if a
  string += ")"

  string
end

def xx_values(hex_string)
  length = hex_string.length

  return hex_string.scan(/./).map { |x| x * 2 } if [3, 4].include?(length)

  hex_string.scan(/../)
end

css = File.open("advanced.css").read

puts parse_css_file(css)
