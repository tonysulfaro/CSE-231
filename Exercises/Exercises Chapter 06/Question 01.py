fp = open('test.txt')
output = ""
for line in fp:
  line = line.strip()
  line = line.replace(" ", "")
  output+=line
print(output)