module Jekyll
  module OrdinalDateFilter
    def ordinal_date(date)
      day = date.strftime("%-d").to_i
      suffix = case day
               when 1, 21, 31 then "st"
               when 2, 22 then "nd"
               when 3, 23 then "rd"
               else "th"
               end
      date.strftime("%-d#{suffix} %B %Y")
    end
  end
end

Liquid::Template.register_filter(Jekyll::OrdinalDateFilter)
