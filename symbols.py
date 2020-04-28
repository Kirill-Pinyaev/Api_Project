print(chr(ord('☀'))) # clear
print(chr(ord('🌤'))) # partly-cloudy, cloudy
print(chr(ord('⛅'))) # overcast
print(chr(ord('🌦'))) # partly-cloudy-and-light-rain, cloudy-and-light-rain, overcast-and-light-rain
print(chr(ord('🌧'))) # partly-cloudy-and-rain, cloudy-and-rain
print(chr(ord('⛆'))) # overcast-and-rain
print(chr(ord('⛈'))) # overcast-thunderstorms-with-rain
print(chr(ord('☔'))) # cloudy-and-rain
print(chr(ord('🌨'))) # overcast-and-wet-snow
print(chr(ord('❄'))) # partly-cloudy-and-snow, cloudy-and-snow
print(chr(ord('❅'))) # partly-cloudy-and-light-snow, cloudy-and-light-snow, overcast-and-light-snow
print(chr(ord('☃'))) # partly-cloudy-and-snow, cloudy-and-snow

condition_d = {"clear": '☀',
               "partly-cloudy": '🌤',
               "cloudy": '⛅',
               "overcast": '🌫️',
               "partly-cloudy-and-light-rain": '🌦',
               "cloudy-and-light-rain": '🌦',
               "overcast-and-light-rain": '🌦',
               "partly-cloudy-and-rain": '🌧',
               "overcast-and-rain": '⛆',
               "overcast-thunderstorms-with-rain": '⛈',
               "cloudy-and-rain": '☔',
               "overcast-and-wet-snow": '🌨',
               "partly-cloudy-and-snow": '❄',
               "cloudy-and-snow": '❄',
               "partly-cloudy-and-light-snow": '❅',
               "cloudy-and-light-snow": '❅',
               "overcast-and-light-snow": '❅',
               "overcast-and-snow": '☃',
               }

print(chr(ord('🌑'))) # new-moon
print(chr(ord('🌗'))) # last-quarter
print(chr(ord('🌕'))) # full-moon
print(chr(ord('🌖'))) # decreasing-moon
print(chr(ord('🌓'))) # first-quarter
print(chr(ord('🌔'))) # growing-moon

print(chr(ord('🌅'))) # sunrise
print(chr(ord('🌇'))) # sunset

print(chr(ord('🕰'))) # clock

print(chr(ord('🌬'))) #wind
wind_direction = {'nw': 'северо-западное',
                  'n': 'северное',
                  'ne': 'северо-восточное',
                  'e': 'восточное',
                  'se': 'юго-восточное',
                  's': 'южное',
                  'sw': 'юго-западное',
                  'w': 'западное',
                  'с': 'штиль'}


print(chr(ord('🧭'))) # compase

print(chr(ord('❄'))) # winter
print(chr(ord('🍂'))) # autumn
print(chr(ord('🍃'))) # summer
print(chr(ord('🌾'))) # spring

print(chr(ord('🌄'))) # polar
print(chr(ord('💫'))) # polar

print(chr(ord('🌡️'))) # thermometer
print(chr(ord('℃'))) # degrees

print(chr(ord('🌙'))) # night
print(chr(ord('☀ '))) # day

fact_d = {"temp": ['🌡', '℃'],
          "condition": '',
          "wind_speed": '📈',
          "wind_dir": '🧭',
          "pressure_mm": '🎇',
          "humidity": '💦'}

time_d = {'0': '🕛', '12': '🕛',
          '1': '🕐', '13': '🕐',
          '2': '🕑', '14': '🕑',
          '3': '🕒', '15': '🕒',
          '4': '🕓', '16': '🕑',
          '5': '🕔', '17': '🕔',
          '6': '🕔', '18': '🕔',
          '7': '🕖', '19': '🕖',
          '8': '🕗', '20': '🕑',
          '9': '🕘', '21': '🕘',
          '10': '🕙', '22': '🕙',
          '11': '🕚', '23': '🕚'
          }