
class Node:
    def __init__(self, x):
        self.value = x
        self.children = []

    def __str__(self, level=0):

        result_list = self.treeDiagramBuilder()
        reverse = result_list[::-1]
        output_str = ''
        protect_index = []

        for line in reverse:

            # 生成修正後的 line
            newline = ''
            for i, c in enumerate(line):
                if (i in protect_index):
                    newline += c
                    if c != '|':
                        protect_index.remove(i)
                else:
                    if c == '|':
                        newline += ' '
                    else:
                        newline += c

            output_str = newline+'\n'+output_str

            # update protect index
            # 與 └ 同一欄的 |，不用替換
            for i, c in enumerate(line):
                if c == '└':
                    protect_index.append(i)

        return output_str

    def treeDiagramBuilder(self, level=0):
        sibling = '|   '
        space = '    '
        result_list = [sibling * (level-1 if level > 1 else 0) +
                       '└───' * (1 if level > 0 else 0) +
                       self.value]
        for i, child in enumerate(self.children):
            line_list = child.treeDiagramBuilder(level + 1)
            result_list += line_list

        return result_list


def testTree():

    w = '''outline, group discussion, handout, research, Proofreading, experiment, written work, report writing, experience, reference, textbook, student advisor, teamwork, module, topic, dictionary, laptop, printer, assessment, library, department, computer centre, classroom, attendance, deadline, give a talk, speech, lecture, tutor, main hall, computer laboratory, certificate, diploma, placement test, facilities, college, dining room, specialist, knowledge, international, accommodation, overseas students, full-time, homestay, primary, secondary, intermediate, media room, commencement, dissertation, leaflet,  school reunion,  feedback, tasks, outcomes, advanced, introductory, extra background, resources room, staff,  higher education, guidelines, post-secondary, faculty, pupils, pencil, supervisor, bachelor’s degree, compound, foreign students, schedule, vocabulary, student support services, student retention, publication,  registrar’s office, stationery'''.replace(
        ' ', '').split(',')

    n_child = 0
    nodequeue = []
    root = Node(w[0])
    node = root

    for c in w[1:]:
        newnode = Node(c)
        node.children.append(newnode)
        nodequeue.append(newnode)
        n_child += 1
        if n_child >= 3:
            node = nodequeue.pop(0)
            n_child = 0

    print(root)


testTree()
