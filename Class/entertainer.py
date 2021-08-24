class Entertainer:
    def __init__(self, name):
        self.name = name

    def set_height(self, height):
        self.height = height

    def set_face(self, face):
        self.face = face

    def set_kind(self, kind): # 인성
        self.kind = kind

    def set_name(self, name):
        self.name = name

    # def info(self):
    #     print(f'이름: {self.name}\t키: {self.height}\t얼굴: {self.face}\t인성: {self.kind}')

    def __str__(self):
        return f'이름: {self.name}\t키: {self.height}\t얼굴: {self.face}\t인성: {self.kind}'

아이유 = Entertainer('아이유')
# 아이유.set_name('이지은')
아이유.set_height('161cm')
아이유.set_face('형섭쌤이상형')
아이유.set_kind("That's very good.") # 'That\'s very good.'
print(아이유)

디노 = Entertainer('이찬')
디노.set_height('172cm')
디노.set_face('아기수달')
디노.set_kind('형만 12명이지만 집안에서는 맏형인 귀염둥이.')
print(디노)

class Singer(Entertainer):
    def __init__(self, name, song):
        super().__init__(name) # self.name = name
        self.song = song

    def __str__(self):
        return super().__str__() + f'\t대표곡: {self.song}'


class Talent(Entertainer):
    def __init__(self, name, drama):
        super().__init__(name)  # self.name = name
        self.drama = drama

    def __str__(self):
        return super().__str__() + f'\t드라마: {self.drama}'

뷔 = Singer('뷔', 'Love Maze')
뷔.set_height('179cm')
뷔.set_face('이지이상형')
뷔.set_kind(f'That\'s very good and cute.')
print(뷔)

RM = Singer('RM', 'Answer: love myself')
RM.set_height('179cm')
RM.set_face('쏘쏘')
RM.set_kind('자기철학이 있어보임')
print(RM)

조슈아 = Singer('Joshua Jisoo Hong', 'ひとりじゃない')
조슈아.set_height('177cm')
조슈아.set_face('꽃사슴')
조슈아.set_kind('N행시 장인 한국계 미국인 좌시')
print(조슈아)

곽동연 = Talent('곽동연', '빈센조')
곽동연.set_height('176cm')
곽동연.set_face('뱀파이어 닮음')
곽동연.set_kind('연기 잘하는 짱 멋진 사람')
print(곽동연)

방탄소년단 = []
방탄소년단.append(뷔)
방탄소년단.append(RM)
print(방탄소년단)
for 멤버 in 방탄소년단:
    print(멤버)

