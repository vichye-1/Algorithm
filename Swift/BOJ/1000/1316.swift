// 단어 개수 받아오기, 단어 개수를 저장하는 'words' 변수 생성
var countInput = Int(readLine()!)!
var words = countInput

// 주어진 단어의 개수만큼 for 문을 돌아 input 단어들을 받음
// arr 라는 빈 배열 생성
for _ in 1...countInput {
  let inputStr = readLine()!
  var arr: [Character] = []

  // 단어 속 알파벳을 순회하며
  // 만약 알파벳이 arr 안에 없으면 arr에 저장
  // arr 안에 있으면 arr에 저장된 마지막 값(바로 앞 알파벳)과 비교해서 같지 않으면(연속되지 않은 값이었다면)
  // arr 안의 모든 요소들을 삭제
  for str in inputStr {
    if !arr.contains(str) { 
      arr.append(str) 
    } else if arr.last != str { 
        arr.removeAll()
        break
      }
    }
    // arr 안의 값이 비어있다면 그룹단어가 아님
    // 따라서 원래 단어 개수(words)에서 -1을 함
    if arr.isEmpty { words -= 1 }
  }  
print(words)
