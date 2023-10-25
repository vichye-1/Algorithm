struct Student {
  var name: String
  var year: Int
  var month: Int
  var day: Int
}

var students = [Student]()

for _ in 1...Int(readLine()!)! {
  let info = readLine()!.split(separator: " ")
  let student = Student(name: String(info[0]), year: Int(info[3])!, month: Int(info[2])!, day: Int(info[1])!)
  students.append(student)
}

students.sort(by: { $0.month == $1.month ? $0.day < $0.day : $0.month < $1.month})
students.sort(by: { $0.year == $1.year ? $0.month < $1.month : $0.year < $1.year})

print(students.last!.name)
print(students.first!.name)
