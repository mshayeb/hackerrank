# https://www.hackerrank.com/challenges/matching-questions-answers

text = gets
text.force_encoding 'UTF-8'
unigram = Hash.new(0)
text.downcase.scan(/\w+/).map{|word| unigram[word] = text.downcase.scan(/\b#{word}\b/).size}
questions_a = Array.new()
questions_h = Hash.new()
answering = Array.new()
for i in 0..4
    answering.push(i)
    question = gets.strip()
    questions_a.push(question)
    questions_h[questions_a[i]] = ""
end
answers = gets;
answers.force_encoding 'UTF-8'
answers = answers.split(";")
for i in 0..4
    questions_a[i].force_encoding 'UTF-8'
    words = questions_a[i].downcase().split(" ")
    bigrams = questions_a[i].split(' ').each_cons(2).to_a
    answered = false
    bigrams.each{|w1, w2|
        s = w1 + " " + w2
        s.gsub!(/\?!,/,"")
        if unigram[w1] <= 2 || unigram[w2] <= 2 && unigram[w1] < 10 && unigram[w2] < 10
            for j in 0..answers.length-1
                if answers[j].downcase().include?(s) || text =~ /(#{s}[\S]* (([\S]* ){1,6})?[\S]*#{answers[j]})|(#{answers[j]}[\S]* (([\S]* ){1,6})?[\S]*#{s})/
                    questions_h[questions_a[i]] = answers[j]
                    answers.delete_at(j)
                    answering.delete(i)
                    answered = true
                    break
                end
            end
        end
        if answered == true
            break
        end
    }
end
to_delete = []
for i in 0..answers.length-1
    ans = answers[i]
    for j in 0..4
        if questions_h[questions_a[j]] == ""
            answered = false
            words = questions_a[j].split(" ")
            bigrams = questions_a[i].split(' ').each_cons(2).to_a
            bigrams.each{|w1, w2|
        		s = w1 + " " + w2
                if unigram[w1] <= 2 && unigram[w2] <= 2
                	s.gsub!(/\?!,/,"")
                    if text =~ /(#{s}[\S]* (([\S]* ){1,6})?[\S]*#{ans})|(#{ans}[\S]* (([\S]* ){1,6})?[\S]*#{s})/
                        questions_h[questions_a[j]] = answers[i]
                        to_delete.push(answers[i])
                        answering.delete(j)
                    	answered = true
                    	break
               		end
                end
                }
        end
        if answered == true
            break
        end
    end
end
to_delete.each{|s|
    answers.delete(s)
    }
answering.each{|i|
    #questions_h[questions_a[i.to_i]] = "NONE"
    questions_h[questions_a[i.to_i]] = answers[0]
    answers.delete_at(0)
    }
for i in 0..4
    puts questions_h[questions_a[i]]
end