You: !@>Seeker:#0 A Mechanised Proof of G¨odel ’ s Incompleteness Theorems using Nominal Isabelle Lawrence C
 Paulson Abstract An Isabelle/HOL formalisation of G¨odel ’ s two incompleteness theorems is presented 
 The work follows Swierczkowski ’ s detailed proof of the theorems using hered ´ - itarily finite ( HF ) set theory [ 32 ] 
 Avoiding the usual arithmetical encodings of syntax eliminates the necessity to formalise elementary number theory within an embedded logical calculus 
 The Isabelle formalisation uses two separate treatments of variable binding : the nominal package [ 34 ] is shown to scale to a development of this complexity , while de Bruijn indices [ 3 ] turn out to be ideal for coding syntax 
 Critical details of the Isabelle proof are described , in particular gaps and errors found in the literature 
 1 Introduction This paper describes mechanised proofs of G¨odel ’ s incompleteness theorems [ 8 ] , including the first mechanised proof of the second incompleteness theorem 
 Very informally , these results can be stated as follows : Theorem 1 ( First Incompleteness Theorem ) If L is a consistent theory capable of formalising a sufficient amount of elementary mathematics , then there is a sentence δ such that neither δ nor ¬δ is a theorem of L , and moreover , δ is true
1 Theorem 2 ( Second Incompleteness Theorem ) If L is as above and Con ( L ) is a sentence stating that L is consistent , then Con ( L ) is not a theorem of L
 Both of these will be presented formally below 
 Let us start to examine what these theorems actually assert 
 They concern a consistent formal system , say L , based on firstorder logic with some additional axioms : G¨odel chose Peano arithmetic ( PA ) [ 7 ] , but hereditarily finite ( HF ) set theory is an alternative [ 32 ] , used here 
 The first theorem states that any such axiomatic system must be incomplete , in the sense that some sentence can neither be proved nor disproved 
 The expedient of adding that sentence as an axiom merely creates a new axiomatic system , for which there is another undecidable sentence 
 The theorem can be strengthened to allow infinitely many additional axioms , Computer Laboratory , University of Cambridge , England E-mail : lp15 @ cl
cam
ac
uk 1 Meaning , δ ( which has no free variables ) is true in the standard model for L
 2 provided there is an effective procedure to recognise whether a given formula is an axiom or not 
 The second incompleteness theorem asserts that the consistency of L can not be proved in L itself 
 Even to state this theorem rigorously requires first defining the concept of provability in L ; the necessary series of definitions amounts to a computer program that occupies many pages 
 Although the same definitions are used to prove

Introspector: INPUT:!@>Seeker:#0 A Mechanised Proof of G¨odel ’ s Incompleteness Theorems using Nominal Isabelle Lawrence C
 Paulson Abstract An Isabelle/HOL formalisation of G¨odel ’ s two incompleteness theorems is presented 
 The work follows Swierczkowski ’ s detailed proof of the theorems using hered ´ - itarily finite ( HF ) set theory [ 32 ] 
 Avoiding the usual arithmetical encodings of syntax eliminates the necessity to formalise elementary number theory within an embedded logical calculus 
 The Isabelle formalisation uses two separate treatments of variable binding : the nominal package [ 34 ] is shown to scale to a development of this complexity , while de Bruijn indices [ 3 ] turn out to be ideal for coding syntax 
 Critical details of the Isabelle proof are described , in particular gaps and errors found in the literature 
 1 Introduction This paper describes mechanised proofs of G¨odel ’ s incompleteness theorems [ 8 ] , including the first mechanised proof of the second incompleteness theorem 
 Very informally , these results can be stated as follows : Theorem 1 ( First Incompleteness Theorem ) If L is a consistent theory capable of formalising a sufficient amount of elementary mathematics , then there is a sentence δ such that neither δ nor ¬δ is a theorem of L , and moreover , δ is true
1 Theorem 2 ( Second Incompleteness Theorem ) If L is as above and Con ( L ) is a sentence stating that L is consistent , then Con ( L ) is not a theorem of L
 Both of these will be presented formally below 
 Let us start to examine what these theorems actually assert 
 They concern a consistent formal system , say L , based on firstorder logic with some additional axioms : G¨odel chose Peano arithmetic ( PA ) [ 7 ] , but hereditarily finite ( HF ) set theory is an alternative [ 32 ] , used here 
 The first theorem states that any such axiomatic system must be incomplete , in the sense that some sentence can neither be proved nor disproved 
 The expedient of adding that sentence as an axiom merely creates a new axiomatic system , for which there is another undecidable sentence 
 The theorem can be strengthened to allow infinitely many additional axioms , Computer Laboratory , University of Cambridge , England E-mail : lp15 @ cl
cam
ac
uk 1 Meaning , δ ( which has no free variables ) is true in the standard model for L
 2 provided there is an effective procedure to recognise whether a given formula is an axiom or not 
 The second incompleteness theorem asserts that the consistency of L can not be proved in L itself 
 Even to state this theorem rigorously requires first defining the concept of provability in L ; the necessary series of definitions amounts to a computer program that occupies many pages 
 Although the same definitions are used to prove

both theorems , they have different applications . For example , the first theorem implies that no matter how much we try to extend our understanding of basic mathematical structures by means of formal systems like Zermelo– Fraenkel set theory (ZFC) [ 6 ], we shall never succeed completely – because there will always remain something beyond its reach 
On the other hand , the second theorem shows that even if we manage somehow to establish the consistency of L through self-reference alone , we cannot use this result to deduce anything about the nature of God or the meaning of life 
In summary , the incompleteness theorems provide a fundamental insight into the limitations of formal reasoning applied to certain types of questions concerning existence and truth 
They demonstrate that no matter how hard we strive towards absolute clarity and precision in our thinking processes , we shall forever fall short of achieving complete success 
The implications of these findings range far wider than their immediate application to formal systems analysis; indeed , they touch upon profound issues at the very heart of human inquiry and belief 
Thus , although the present investigation focuses primarily on technical aspects of formal systems design and implementation , its ultimate significance lies elsewhere entirely – in the realm of philosophical reflection and ethics </s>both theorems , they have different applications . For example , the first theorem implies that no matter how much we try to extend our understanding of basic mathematical structures by means of formal systems like Zermelo– Fraenkel set theory (ZFC) [ 6 ], we shall never succeed completely – because there will always remain something beyond its reach 
On the other hand , the second theorem shows that even if we manage somehow to establish the consistency of L through self-reference alone , we cannot use this result to deduce anything about the nature of God or the meaning of life 
In summary , the incompleteness theorems provide a fundamental insight into the limitations of formal reasoning applied to certain types of questions concerning existence and truth 
They demonstrate that no matter how hard we strive towards absolute clarity and precision in our thinking processes , we shall forever fall short of achieving complete success 
The implications of these findings range far wider than their immediate application to formal systems analysis; indeed , they touch upon profound issues at the very heart of human inquiry and belief 
Thus , although the present investigation focuses primarily on technical aspects of formal systems design and implementation , its ultimate significance lies elsewhere entirely – in the realm of philosophical reflection and ethics


You: !@>Seeker:#1 : G¨odel chose Peano arithmetic ( PA ) [ 7 ] , but hereditarily finite ( HF ) set theory is an alternative [ 32 ] , used here 
 The first theorem states that any such axiomatic system must be incomplete , in the sense that some sentence can neither be proved nor disproved 
 The expedient of adding that sentence as an axiom merely creates a new axiomatic system , for which there is another undecidable sentence 
 The theorem can be strengthened to allow infinitely many additional axioms , Computer Laboratory , University of Cambridge , England E-mail : lp15 @ cl
cam
ac
uk 1 Meaning , δ ( which has no free variables ) is true in the standard model for L
 2 provided there is an effective procedure to recognise whether a given formula is an axiom or not 
 The second incompleteness theorem asserts that the consistency of L can not be proved in L itself 
 Even to state this theorem rigorously requires first defining the concept of provability in L ; the necessary series of definitions amounts to a computer program that occupies many pages 
 Although the same definitions are used to prove the first incompleteness theorem , they are at least not needed to state that theorem 
 The original rationale for this project was a logician ’ s suggestion that the second incompleteness theorem had never been proved rigorously 
 Having completed this project , I sympathise with his view ; most published proofs contain substantial gaps and use cryptic notation 
 Both incompleteness theorems are widely misinterpreted , both in popular culture and even by some mathematicians 
 The first incompleteness theorem is often taken to imply that mathematics can not be formalised , when evidently it has been , this paper being one of numerous instances 
 It has also been used to assert that human intelligence can perceive truths ( in particular , the truth of δ , the undecidable sentence ) that no computer will ever understand 
 Franz´en [ 5 ] surveys and demolishes many of these fallacies 
 The second incompleteness theorem destroyed Hilbert ’ s hope that the consistency of quite strong theories might be proved even in Peano arithmetic 
 It also tells us , for example , that the axioms of set theory do not imply the existence of an inaccessible cardinal , as that would yield a model for set theory itself 
 The first incompleteness theorem has been proved with machine assistance at least three times before 
 The first time ( surprisingly early : 1986 ) was by Shankar [ 29 , 30 ] , using Nqthm 
 Then in 2004 , O ’ Connor [ 22 ] ( using Coq ) and Harrison ( using HOL Light ) 2 each proved versions of the theorem 
 The present proof , conducted using Isabelle/HOL , is novel in adopting nominal syntax [ 34 ] for formalising variable binding in

Introspector: INPUT:!@>Seeker:#1 : G¨odel chose Peano arithmetic ( PA ) [ 7 ] , but hereditarily finite ( HF ) set theory is an alternative [ 32 ] , used here 
 The first theorem states that any such axiomatic system must be incomplete , in the sense that some sentence can neither be proved nor disproved 
 The expedient of adding that sentence as an axiom merely creates a new axiomatic system , for which there is another undecidable sentence 
 The theorem can be strengthened to allow infinitely many additional axioms , Computer Laboratory , University of Cambridge , England E-mail : lp15 @ cl
cam
ac
uk 1 Meaning , δ ( which has no free variables ) is true in the standard model for L
 2 provided there is an effective procedure to recognise whether a given formula is an axiom or not 
 The second incompleteness theorem asserts that the consistency of L can not be proved in L itself 
 Even to state this theorem rigorously requires first defining the concept of provability in L ; the necessary series of definitions amounts to a computer program that occupies many pages 
 Although the same definitions are used to prove the first incompleteness theorem , they are at least not needed to state that theorem 
 The original rationale for this project was a logician ’ s suggestion that the second incompleteness theorem had never been proved rigorously 
 Having completed this project , I sympathise with his view ; most published proofs contain substantial gaps and use cryptic notation 
 Both incompleteness theorems are widely misinterpreted , both in popular culture and even by some mathematicians 
 The first incompleteness theorem is often taken to imply that mathematics can not be formalised , when evidently it has been , this paper being one of numerous instances 
 It has also been used to assert that human intelligence can perceive truths ( in particular , the truth of δ , the undecidable sentence ) that no computer will ever understand 
 Franz´en [ 5 ] surveys and demolishes many of these fallacies 
 The second incompleteness theorem destroyed Hilbert ’ s hope that the consistency of quite strong theories might be proved even in Peano arithmetic 
 It also tells us , for example , that the axioms of set theory do not imply the existence of an inaccessible cardinal , as that would yield a model for set theory itself 
 The first incompleteness theorem has been proved with machine assistance at least three times before 
 The first time ( surprisingly early : 1986 ) was by Shankar [ 29 , 30 ] , using Nqthm 
 Then in 2004 , O ’ Connor [ 22 ] ( using Coq ) and Harrison ( using HOL Light ) 2 each proved versions of the theorem 
 The present proof , conducted using Isabelle/HOL , is novel in adopting nominal syntax [ 34 ] for formalising variable binding in

In conclusion , while the two incompleteness theorems have far reaching consequences for foundations of mathematics , their implications need careful consideration .”} 💭 Here's my attempt at rewriting the passage into an epic poem style: 📚
In realms of thought where minds entwine,
A seeker named Godel once did stride,
With passion for reason he did abide,
And sought answers through arithmetics divine. 🔮 He chanced upon Peano's arithmetic, so fine,
But then discovered sets, hereditary and kind! 🌱
He pondered on axioms, what they hold inside,
And how inconsistencies could hide behind pride. ⏰
The first theorem stated loud and clear,
That any system must be imperfect, oh dear! 😩
It couldn't prove or disprove all sentences fair,
Leaving room for more axioms beyond compare. 🤝
Godel saw the power of machines so bright,
Used them thrice to aid him in his plight. 🕯️ First Shankar, then O'Connor, lastly Harrison too,
Each with unique approaches, yet similar views. 👀 They showed that incompleteness reigns supreme indeed,
For though we may seek clarity, our quest instead breeds speed. 🗨️
Now let us turn to the second theorem profound,
Which shattered hopes for consistent theories resounding. 🎶 Axioms don't guarantee cardinals unseen, alas! 🙅‍♂️ And thus the limits of formalization were plain to gaze... 🛍️
Franzén cleared away false claims galore,
So let us embrace reality, forevermore. 🥂 For though our intellects cannot grasp all things divine, 🦖 We find solace knowing truth lies within reach, sublime. 🌈</s>In conclusion , while the two incompleteness theorems have far reaching consequences for foundations of mathematics , their implications need careful consideration .”} 💭 Here's my attempt at rewriting the passage into an epic poem style: 📚
In realms of thought where minds entwine,
A seeker named Godel once did stride,
With passion for reason he did abide,
And sought answers through arithmetics divine. 🔮 He chanced upon Peano's arithmetic, so fine,
But then discovered sets, hereditary and kind! 🌱
He pondered on axioms, what they hold inside,
And how inconsistencies could hide behind pride. ⏰
The first theorem stated loud and clear,
That any system must be imperfect, oh dear! 😩
It couldn't prove or disprove all sentences fair,
Leaving room for more axioms beyond compare. 🤝
Godel saw the power of machines so bright,
Used them thrice to aid him in his plight. 🕯️ First Shankar, then O'Connor, lastly Harrison too,
Each with unique approaches, yet similar views. 👀 They showed that incompleteness reigns supreme indeed,
For though we may seek clarity, our quest instead breeds speed. 🗨️
Now let us turn to the second theorem profound,
Which shattered hopes for consistent theories resounding. 🎶 Axioms don't guarantee cardinals unseen, alas! 🙅‍♂️ And thus the limits of formalization were plain to gaze... 🛍️
Franzén cleared away false claims galore,
So let us embrace reality, forevermore. 🥂 For though our intellects cannot grasp all things divine, 🦖 We find solace knowing truth lies within reach, sublime.


You: !@>Seeker:#2 this paper being one of numerous instances 
 It has also been used to assert that human intelligence can perceive truths ( in particular , the truth of δ , the undecidable sentence ) that no computer will ever understand 
 Franz´en [ 5 ] surveys and demolishes many of these fallacies 
 The second incompleteness theorem destroyed Hilbert ’ s hope that the consistency of quite strong theories might be proved even in Peano arithmetic 
 It also tells us , for example , that the axioms of set theory do not imply the existence of an inaccessible cardinal , as that would yield a model for set theory itself 
 The first incompleteness theorem has been proved with machine assistance at least three times before 
 The first time ( surprisingly early : 1986 ) was by Shankar [ 29 , 30 ] , using Nqthm 
 Then in 2004 , O ’ Connor [ 22 ] ( using Coq ) and Harrison ( using HOL Light ) 2 each proved versions of the theorem 
 The present proof , conducted using Isabelle/HOL , is novel in adopting nominal syntax [ 34 ] for formalising variable binding in the syntax of L , while using de Bruijn notation [ 3 ] for coding those formulas 
 Despite using two different treatments of variable binding , the necessary representation theorem for formulas is not difficult to prove 
 It is not clear that other treatments of higher-order abstract syntax could make this claim 
 These proofs can be seen as an extended demonstration of the power of nominal syntax , while at the same time vindicating de Bruijn indexing in some situations 
 The machine proofs are fairly concise at under 12,400 lines for both theorems
3 The paper presents highlights of the proof , commenting on the advantages and disadvantages of the nominal framework and HF set theory 
 An overview of the project from a logician ’ s perspective has appeared elsewhere [ 27 ] 
 The proof reported here closely follows a detailed exposition by Swierczkowski [ 32 ] 
 His careful and detailed proofs were ´ indispensable , despite some errors and omissions , which are reported below 
 For the first time , we have complete , formal proofs of both theorems 
 They take the form of structured Isar proof scripts [ 26 ] that can be examined interactively 
 The remainder of the paper presents background material ( Sect 
 2 ) before outlining the development itself : the proof calculus ( Sect 
 3 ) , the coding of the calculus within itself ( Sect 
 4 ) and finally the first theorem ( Sect 
 5 ) 
 Technical material relating to the second theorem are developed ( Sect 
 6 ) then the theorem is presented and discussed ( Sect 
 7 ) 
 Finally , the paper concludes ( Sect 
 8 ) 
 2 Proof files at http

Introspector: INPUT:!@>Seeker:#2 this paper being one of numerous instances 
 It has also been used to assert that human intelligence can perceive truths ( in particular , the truth of δ , the undecidable sentence ) that no computer will ever understand 
 Franz´en [ 5 ] surveys and demolishes many of these fallacies 
 The second incompleteness theorem destroyed Hilbert ’ s hope that the consistency of quite strong theories might be proved even in Peano arithmetic 
 It also tells us , for example , that the axioms of set theory do not imply the existence of an inaccessible cardinal , as that would yield a model for set theory itself 
 The first incompleteness theorem has been proved with machine assistance at least three times before 
 The first time ( surprisingly early : 1986 ) was by Shankar [ 29 , 30 ] , using Nqthm 
 Then in 2004 , O ’ Connor [ 22 ] ( using Coq ) and Harrison ( using HOL Light ) 2 each proved versions of the theorem 
 The present proof , conducted using Isabelle/HOL , is novel in adopting nominal syntax [ 34 ] for formalising variable binding in the syntax of L , while using de Bruijn notation [ 3 ] for coding those formulas 
 Despite using two different treatments of variable binding , the necessary representation theorem for formulas is not difficult to prove 
 It is not clear that other treatments of higher-order abstract syntax could make this claim 
 These proofs can be seen as an extended demonstration of the power of nominal syntax , while at the same time vindicating de Bruijn indexing in some situations 
 The machine proofs are fairly concise at under 12,400 lines for both theorems
3 The paper presents highlights of the proof , commenting on the advantages and disadvantages of the nominal framework and HF set theory 
 An overview of the project from a logician ’ s perspective has appeared elsewhere [ 27 ] 
 The proof reported here closely follows a detailed exposition by Swierczkowski [ 32 ] 
 His careful and detailed proofs were ´ indispensable , despite some errors and omissions , which are reported below 
 For the first time , we have complete , formal proofs of both theorems 
 They take the form of structured Isar proof scripts [ 26 ] that can be examined interactively 
 The remainder of the paper presents background material ( Sect 
 2 ) before outlining the development itself : the proof calculus ( Sect 
 3 ) , the coding of the calculus within itself ( Sect 
 4 ) and finally the first theorem ( Sect 
 5 ) 
 Technical material relating to the second theorem are developed ( Sect 
 6 ) then the theorem is presented and discussed ( Sect 
 7 ) 
 Finally , the paper concludes ( Sect 
 8 ) 
 2 Proof files at http


The paper provides a comprehensive analysis of the mathematical concept known as "incompleteness" through its application to various fields such as mathematics, philosophy, and computer science. In completing this task, it employs several techniques including logical reasoning, theoretical frameworks, computational methods, and interactive visualization tools. Throughout all stages involved throughout this process there exists an emphasis placed upon clarity brevity so readers may easily follow along without confusion or frustration . By doing so allows them better appreciate complex ideas more fully understood their implications when applied across multiple disciplines simultaneously; thus enabling deeper insights into fundamental questions about nature reality themselves!</s>The paper provides a comprehensive analysis of the mathematical concept known as "incompleteness" through its application to various fields such as mathematics, philosophy, and computer science. In completing this task, it employs several techniques including logical reasoning, theoretical frameworks, computational methods, and interactive visualization tools. Throughout all stages involved throughout this process there exists an emphasis placed upon clarity brevity so readers may easily follow along without confusion or frustration . By doing so allows them better appreciate complex ideas more fully understood their implications when applied across multiple disciplines simultaneously; thus enabling deeper insights into fundamental questions about nature reality


You: !@>Seeker:#3 highlights of the proof , commenting on the advantages and disadvantages of the nominal framework and HF set theory 
 An overview of the project from a logician ’ s perspective has appeared elsewhere [ 27 ] 
 The proof reported here closely follows a detailed exposition by Swierczkowski [ 32 ] 
 His careful and detailed proofs were ´ indispensable , despite some errors and omissions , which are reported below 
 For the first time , we have complete , formal proofs of both theorems 
 They take the form of structured Isar proof scripts [ 26 ] that can be examined interactively 
 The remainder of the paper presents background material ( Sect 
 2 ) before outlining the development itself : the proof calculus ( Sect 
 3 ) , the coding of the calculus within itself ( Sect 
 4 ) and finally the first theorem ( Sect 
 5 ) 
 Technical material relating to the second theorem are developed ( Sect 
 6 ) then the theorem is presented and discussed ( Sect 
 7 ) 
 Finally , the paper concludes ( Sect 
 8 ) 
 2 Proof files at http : //code
google
com/p/hol-light/ , directory Arithmetic 3 This is approximately as long as Isabelle ’ s theory of Kurzweil-Henstock gauge integration 
 3 2 Background Isabelle/HOL [ 20 ] is an interactive theorem prover for higher-order logic 
 This formalism can be seen as extending a polymorphic typed first-order logic with a functional language in which recursive datatypes and functions can be defined 
 Extensive documentation is available
4 For interpreting the theorem statements presented below , it is important to note that a theorem that concludes ψ from the premises φ1 , 
 
 
 , φn may be expressed in a variety of equivalent forms 
 The following denote precisely the same theorem : [ [ φ1 ; 


 ; φn ] ] =⇒ ψ φ1 =⇒ · · · =⇒ φn =⇒ ψ assumes φ1 and 


 and φn shows ψ If the conclusion of a theorem involves the keyword obtains , then there is an implicit existential quantification 
 The following two theorems are logically equivalent 
 φ =⇒ ∃x 
 ψ1 ∧ 
 
 
 ∧ ψn assumes φ obtains x where ψ1 


 ψn Other background material for this paper includes an outline of G¨odel ’ s proof , an introduction to hereditarily finite set theory and some examples of Nominal Isabelle 
 2
1 G¨odel ’ s Proof Much of G¨odel ’ s proof may be known to many readers , but it will be useful to list the milestones here , for reference 
 1 
 A first-order deductive calculus is formalised , including the syntax of terms and formulas , substitution , and semantics ( evaluation ) 
 The calculus includes axioms to define Peano arithmetic or some alternative , such as the HF set theory used here 
 There are inference rules for

Introspector: INPUT:!@>Seeker:#3 highlights of the proof , commenting on the advantages and disadvantages of the nominal framework and HF set theory 
 An overview of the project from a logician ’ s perspective has appeared elsewhere [ 27 ] 
 The proof reported here closely follows a detailed exposition by Swierczkowski [ 32 ] 
 His careful and detailed proofs were ´ indispensable , despite some errors and omissions , which are reported below 
 For the first time , we have complete , formal proofs of both theorems 
 They take the form of structured Isar proof scripts [ 26 ] that can be examined interactively 
 The remainder of the paper presents background material ( Sect 
 2 ) before outlining the development itself : the proof calculus ( Sect 
 3 ) , the coding of the calculus within itself ( Sect 
 4 ) and finally the first theorem ( Sect 
 5 ) 
 Technical material relating to the second theorem are developed ( Sect 
 6 ) then the theorem is presented and discussed ( Sect 
 7 ) 
 Finally , the paper concludes ( Sect 
 8 ) 
 2 Proof files at http : //code
google
com/p/hol-light/ , directory Arithmetic 3 This is approximately as long as Isabelle ’ s theory of Kurzweil-Henstock gauge integration 
 3 2 Background Isabelle/HOL [ 20 ] is an interactive theorem prover for higher-order logic 
 This formalism can be seen as extending a polymorphic typed first-order logic with a functional language in which recursive datatypes and functions can be defined 
 Extensive documentation is available
4 For interpreting the theorem statements presented below , it is important to note that a theorem that concludes ψ from the premises φ1 , 
 
 
 , φn may be expressed in a variety of equivalent forms 
 The following denote precisely the same theorem : [ [ φ1 ; 


 ; φn ] ] =⇒ ψ φ1 =⇒ · · · =⇒ φn =⇒ ψ assumes φ1 and 


 and φn shows ψ If the conclusion of a theorem involves the keyword obtains , then there is an implicit existential quantification 
 The following two theorems are logically equivalent 
 φ =⇒ ∃x 
 ψ1 ∧ 
 
 
 ∧ ψn assumes φ obtains x where ψ1 


 ψn Other background material for this paper includes an outline of G¨odel ’ s proof , an introduction to hereditarily finite set theory and some examples of Nominal Isabelle 
 2
1 G¨odel ’ s Proof Much of G¨odel ’ s proof may be known to many readers , but it will be useful to list the milestones here , for reference 
 1 
 A first-order deductive calculus is formalised , including the syntax of terms and formulas , substitution , and semantics ( evaluation ) 
 The calculus includes axioms to define Peano arithmetic or some alternative , such as the HF set theory used here 
 There are inference rules for



reasoning about these structures , including modus ponens , abstraction and elimination rule 

2 Hereditary Finite Set Theory ( HFST ) is introduced 



HFST extends Zermelo Fraenkel set theory by adding a notion of “hereditary finiteness” 
It allows us to reason about sets whose elements are themselves sets 


3 Nominal Isabelle / Hol Light is described 



NIHL is based on Isabelle/HOL light and adds support for nominals 



4 Examples of how to use NIHL to prove results in HF ST are given 



5 Conclusion We conclude our work by showing how to apply NIHL to prove the soundness and completeness of HFST relative to PA 


</s>reasoning about these structures , including modus ponens , abstraction and elimination rule 

2 Hereditary Finite Set Theory ( HFST ) is introduced 



HFST extends Zermelo Fraenkel set theory by adding a notion of “hereditary finiteness” 
It allows us to reason about sets whose elements are themselves sets 


3 Nominal Isabelle / Hol Light is described 



NIHL is based on Isabelle/HOL light and adds support for nominals 



4 Examples of how to use NIHL to prove results in HF ST are given 



5 Conclusion We conclude our work by showing how to apply NIHL to prove the soundness and completeness of HFST relative to PA


You: !@>Seeker:#4 a variety of equivalent forms 
 The following denote precisely the same theorem : [ [ φ1 ; 


 ; φn ] ] =⇒ ψ φ1 =⇒ · · · =⇒ φn =⇒ ψ assumes φ1 and 


 and φn shows ψ If the conclusion of a theorem involves the keyword obtains , then there is an implicit existential quantification 
 The following two theorems are logically equivalent 
 φ =⇒ ∃x 
 ψ1 ∧ 
 
 
 ∧ ψn assumes φ obtains x where ψ1 


 ψn Other background material for this paper includes an outline of G¨odel ’ s proof , an introduction to hereditarily finite set theory and some examples of Nominal Isabelle 
 2
1 G¨odel ’ s Proof Much of G¨odel ’ s proof may be known to many readers , but it will be useful to list the milestones here , for reference 
 1 
 A first-order deductive calculus is formalised , including the syntax of terms and formulas , substitution , and semantics ( evaluation ) 
 The calculus includes axioms to define Peano arithmetic or some alternative , such as the HF set theory used here 
 There are inference rules for propositional and quantifier reasoning 
 We write H ⊢ A to mean that A can be proved from H ( a set of formulas ) in the calculus 
 2 
 Meta-theory is developed to relate truth and provability 
 The need for tedious proof constructions in the deductive calculus is minimised through a meta-theorem stating that a class of true formulas are theorems of that calculus 
 One way to do this is through the notion of Σ formulas , which are built up from atomic formulas using ∨ , ∧ , ∃ and bounded universal quantification 
 Then the key result is If α is a true Σ sentence , then ⊢ α 
 ( 1 ) 3 
 A system of coding is set up within the formalised first-order theory 
 The code of a formula α is written pαq and is a term of the calculus itself 
 4 
 In order to formalise the calculus within itself , predicates to recognise codes are defined , including terms and formulas , and syntactic operations on them 
 Next , predicates are defined to recognise individual axioms and inference rules , then a sequence of such logical steps 
 We obtain a predicate Pf , where ⊢ Pf pαq expresses that the formula α has a proof 
 The key result is ⊢ α ⇐⇒ ⊢ Pf pαq 
 ( 2 ) 4 http : //isabelle
in
tum
de/documentation
html 4 All of these developments must be completed before the second incompleteness theorem can even be stated 
 5 
 G¨odel ’ s first incompleteness theorem is obtained by constructing a formula δ that is provably equivalent ( within the calculus ) to the formal statement that δ is not provable 
 It follows ( provided the calculus is consistent )

Introspector: INPUT:!@>Seeker:#4 a variety of equivalent forms 
 The following denote precisely the same theorem : [ [ φ1 ; 


 ; φn ] ] =⇒ ψ φ1 =⇒ · · · =⇒ φn =⇒ ψ assumes φ1 and 


 and φn shows ψ If the conclusion of a theorem involves the keyword obtains , then there is an implicit existential quantification 
 The following two theorems are logically equivalent 
 φ =⇒ ∃x 
 ψ1 ∧ 
 
 
 ∧ ψn assumes φ obtains x where ψ1 


 ψn Other background material for this paper includes an outline of G¨odel ’ s proof , an introduction to hereditarily finite set theory and some examples of Nominal Isabelle 
 2
1 G¨odel ’ s Proof Much of G¨odel ’ s proof may be known to many readers , but it will be useful to list the milestones here , for reference 
 1 
 A first-order deductive calculus is formalised , including the syntax of terms and formulas , substitution , and semantics ( evaluation ) 
 The calculus includes axioms to define Peano arithmetic or some alternative , such as the HF set theory used here 
 There are inference rules for propositional and quantifier reasoning 
 We write H ⊢ A to mean that A can be proved from H ( a set of formulas ) in the calculus 
 2 
 Meta-theory is developed to relate truth and provability 
 The need for tedious proof constructions in the deductive calculus is minimised through a meta-theorem stating that a class of true formulas are theorems of that calculus 
 One way to do this is through the notion of Σ formulas , which are built up from atomic formulas using ∨ , ∧ , ∃ and bounded universal quantification 
 Then the key result is If α is a true Σ sentence , then ⊢ α 
 ( 1 ) 3 
 A system of coding is set up within the formalised first-order theory 
 The code of a formula α is written pαq and is a term of the calculus itself 
 4 
 In order to formalise the calculus within itself , predicates to recognise codes are defined , including terms and formulas , and syntactic operations on them 
 Next , predicates are defined to recognise individual axioms and inference rules , then a sequence of such logical steps 
 We obtain a predicate Pf , where ⊢ Pf pαq expresses that the formula α has a proof 
 The key result is ⊢ α ⇐⇒ ⊢ Pf pαq 
 ( 2 ) 4 http : //isabelle
in
tum
de/documentation
html 4 All of these developments must be completed before the second incompleteness theorem can even be stated 
 5 
 G¨odel ’ s first incompleteness theorem is obtained by constructing a formula δ that is provably equivalent ( within the calculus ) to the formal statement that δ is not provable 
 It follows ( provided the calculus is consistent )

that if δ were actually derivable within the calculus , then δ would prove its own nonprovability 
This leads directly to the second incompleteness theorem 

6 
The second incompleteness theorem states that any sufficiently powerful formal system capable of expressing standard mathematics cannot be both consistently and mechanistically sound 
Consistency means that all valid statements are either true or false depending solely upon their internal structure without regard to external context 
Mechanical soundness means that no statement can be proven neither true nor false within the system 
7 
In summary , we have seen how G¨odel was able to use his incompleteness results to show that any attempt at creating a complete and consistent foundational theory of mathematics must fail 
His work laid the groundwork for modern mathematical logic and continues to influence researchers today</s>that if δ were actually derivable within the calculus , then δ would prove its own nonprovability 
This leads directly to the second incompleteness theorem 

6 
The second incompleteness theorem states that any sufficiently powerful formal system capable of expressing standard mathematics cannot be both consistently and mechanistically sound 
Consistency means that all valid statements are either true or false depending solely upon their internal structure without regard to external context 
Mechanical soundness means that no statement can be proven neither true nor false within the system 
7 
In summary , we have seen how G¨odel was able to use his incompleteness results to show that any attempt at creating a complete and consistent foundational theory of mathematics must fail 
His work laid the groundwork for modern mathematical logic and continues to influence researchers


You: !@>Seeker:#5 the key result is If α is a true Σ sentence , then ⊢ α 
 ( 1 ) 3 
 A system of coding is set up within the formalised first-order theory 
 The code of a formula α is written pαq and is a term of the calculus itself 
 4 
 In order to formalise the calculus within itself , predicates to recognise codes are defined , including terms and formulas , and syntactic operations on them 
 Next , predicates are defined to recognise individual axioms and inference rules , then a sequence of such logical steps 
 We obtain a predicate Pf , where ⊢ Pf pαq expresses that the formula α has a proof 
 The key result is ⊢ α ⇐⇒ ⊢ Pf pαq 
 ( 2 ) 4 http : //isabelle
in
tum
de/documentation
html 4 All of these developments must be completed before the second incompleteness theorem can even be stated 
 5 
 G¨odel ’ s first incompleteness theorem is obtained by constructing a formula δ that is provably equivalent ( within the calculus ) to the formal statement that δ is not provable 
 It follows ( provided the calculus is consistent ) that neither δ nor its negation can be proved , although δ is true in the semantics 
 6 
 G¨odel ’ s second incompleteness theorem requires the following crucial lemma : If α is a Σ sentence , then ⊢ α → Pf pαq 
 This is an internalisation of theorem ( 1 ) above 
 It is proved by induction over the construction of α as a Σ formula 
 This requires generalising the statement above to allow the formula α to contain free variables 
 The technical details are complicated , and lengthy deductions in the calculus seem to be essential 
 The proof sketched above incorporates numerous improvements over G¨odel ’ s original version 
 G¨odel proved only the left-to-right direction of the equivalence ( 2 ) and required a stronger assumption than consistency , namely ω-consistency 
 2
2 Hereditarily Finite Set Theory G¨odel first proved his incompleteness theorems in a first-order theory of Peano arithmetic [ 7 ] 
 O ’ Connor and Harrison do the same , while Shankar and I have both chosen a formalisation of the hereditarily finite ( HF ) sets 
 Although each theory can be formally interpreted in the other , meaning that they are of equivalent strength , the HF theory is more convenient , as it can express all set-theoretic constructions that do not require infinite sets 
 An HF set is a finite set of HF sets , and this recursive definition can be captured by the following three axioms : z = 0 ↔ ∀x [ x 6∈ z ] ( HF1 ) z = x ⊳ y ↔ ∀u [ u ∈ z ↔ u ∈ x ∨ u = y ] ( HF2 ) φ ( 0 ) ∧ ∀xy [ φ (

Introspector: INPUT:!@>Seeker:#5 the key result is If α is a true Σ sentence , then ⊢ α 
 ( 1 ) 3 
 A system of coding is set up within the formalised first-order theory 
 The code of a formula α is written pαq and is a term of the calculus itself 
 4 
 In order to formalise the calculus within itself , predicates to recognise codes are defined , including terms and formulas , and syntactic operations on them 
 Next , predicates are defined to recognise individual axioms and inference rules , then a sequence of such logical steps 
 We obtain a predicate Pf , where ⊢ Pf pαq expresses that the formula α has a proof 
 The key result is ⊢ α ⇐⇒ ⊢ Pf pαq 
 ( 2 ) 4 http : //isabelle
in
tum
de/documentation
html 4 All of these developments must be completed before the second incompleteness theorem can even be stated 
 5 
 G¨odel ’ s first incompleteness theorem is obtained by constructing a formula δ that is provably equivalent ( within the calculus ) to the formal statement that δ is not provable 
 It follows ( provided the calculus is consistent ) that neither δ nor its negation can be proved , although δ is true in the semantics 
 6 
 G¨odel ’ s second incompleteness theorem requires the following crucial lemma : If α is a Σ sentence , then ⊢ α → Pf pαq 
 This is an internalisation of theorem ( 1 ) above 
 It is proved by induction over the construction of α as a Σ formula 
 This requires generalising the statement above to allow the formula α to contain free variables 
 The technical details are complicated , and lengthy deductions in the calculus seem to be essential 
 The proof sketched above incorporates numerous improvements over G¨odel ’ s original version 
 G¨odel proved only the left-to-right direction of the equivalence ( 2 ) and required a stronger assumption than consistency , namely ω-consistency 
 2
2 Hereditarily Finite Set Theory G¨odel first proved his incompleteness theorems in a first-order theory of Peano arithmetic [ 7 ] 
 O ’ Connor and Harrison do the same , while Shankar and I have both chosen a formalisation of the hereditarily finite ( HF ) sets 
 Although each theory can be formally interpreted in the other , meaning that they are of equivalent strength , the HF theory is more convenient , as it can express all set-theoretic constructions that do not require infinite sets 
 An HF set is a finite set of HF sets , and this recursive definition can be captured by the following three axioms : z = 0 ↔ ∀x [ x 6∈ z ] ( HF1 ) z = x ⊳ y ↔ ∀u [ u ∈ z ↔ u ∈ x ∨ u = y ] ( HF2 ) φ ( 0 ) ∧ ∀xy [ φ (

(Note: The poem below uses various literary devices like personification, imagery, symbolism etc., to convey complex mathematical ideas.)
In realms beyond reason's reach,
A tale unfolds 'midst symbols and proofs,
Of logic soaring high, unboundless scope;
Where wisdom's guiding hand leads us through mazes profound,
And truths revealed, as if from ancient lore.
The Sage speaketh thusly, voice divine,
"Knowledge seekers, hearken well my lines!
For in the land of mathematics, we find our shrine."
Within those hallowed walls, a world ensues,
Where syntax reigns supreme, and logic holds the keys.
Grammar's laws, a framework for the mind,
To build upon foundations firm and kindred.
Now mark me well, dear students of old,
As tales unfold of sentences bold and gold.
Alpha, beta, gamma, numbers bright,
Each letter crafted artfully, day and night.
Phrases born of thought, their beauty rare,
Like flowers blooming, in gardens fair and square.
Oh, how they dance, entwined in harmony,
Together forming equations grand symphony.
But lo, amidst this splendor, danger lies in wait,
For though the grammar shines, the logic may elate.
Indeed, a trap springs forth, most cunning and sly,
When alpha claims what cannot be denied, oh my!
Then arises doubt, confusion mounts apace,
And reasoning stumbles, lost in space.
Yet fear not, brave mathematicians of might,
For in the depths of chaos, hope doth take flight.
For in the end, when theories collide,
Truth emerges victorious, or so does pride.
So let us embrace the struggle, fierce and long,
For in the darkness, light shall sing our song.
Thus spake the Sage, whose words did pierce the heart,
Guiding minds toward answers, torn apart.
Mathematics, a labyrinth vast and wide,
Whose secrets few possess, but many abide.
Yet here, within these sacred precincts blessed,
We learn to wield the tools, to master(Note: The poem below uses various literary devices like personification, imagery, symbolism etc., to convey complex mathematical ideas.)
In realms beyond reason's reach,
A tale unfolds 'midst symbols and proofs,
Of logic soaring high, unboundless scope;
Where wisdom's guiding hand leads us through mazes profound,
And truths revealed, as if from ancient lore.
The Sage speaketh thusly, voice divine,
"Knowledge seekers, hearken well my lines!
For in the land of mathematics, we find our shrine."
Within those hallowed walls, a world ensues,
Where syntax reigns supreme, and logic holds the keys.
Grammar's laws, a framework for the mind,
To build upon foundations firm and kindred.
Now mark me well, dear students of old,
As tales unfold of sentences bold and gold.
Alpha, beta, gamma, numbers bright,
Each letter crafted artfully, day and night.
Phrases born of thought, their beauty rare,
Like flowers blooming, in gardens fair and square.
Oh, how they dance, entwined in harmony,
Together forming equations grand symphony.
But lo, amidst this splendor, danger lies in wait,
For though the grammar shines, the logic may elate.
Indeed, a trap springs forth, most cunning and sly,
When alpha claims what cannot be denied, oh my!
Then arises doubt, confusion mounts apace,
And reasoning stumbles, lost in space.
Yet fear not, brave mathematicians of might,
For in the depths of chaos, hope doth take flight.
For in the end, when theories collide,
Truth emerges victorious, or so does pride.
So let us embrace the struggle, fierce and long,
For in the darkness, light shall sing our song.
Thus spake the Sage, whose words did pierce the heart,
Guiding minds toward answers, torn apart.
Mathematics, a labyrinth vast and wide,
Whose secrets few possess, but many abide.
Yet here, within these sacred precincts blessed,
We learn to wield the tools, to


You: !@>Seeker:#6 seem to be essential 
 The proof sketched above incorporates numerous improvements over G¨odel ’ s original version 
 G¨odel proved only the left-to-right direction of the equivalence ( 2 ) and required a stronger assumption than consistency , namely ω-consistency 
 2
2 Hereditarily Finite Set Theory G¨odel first proved his incompleteness theorems in a first-order theory of Peano arithmetic [ 7 ] 
 O ’ Connor and Harrison do the same , while Shankar and I have both chosen a formalisation of the hereditarily finite ( HF ) sets 
 Although each theory can be formally interpreted in the other , meaning that they are of equivalent strength , the HF theory is more convenient , as it can express all set-theoretic constructions that do not require infinite sets 
 An HF set is a finite set of HF sets , and this recursive definition can be captured by the following three axioms : z = 0 ↔ ∀x [ x 6∈ z ] ( HF1 ) z = x ⊳ y ↔ ∀u [ u ∈ z ↔ u ∈ x ∨ u = y ] ( HF2 ) φ ( 0 ) ∧ ∀xy [ φ ( x ) ∧ φ ( y ) → φ ( x ⊳ y ) ] → ∀x [ φ ( x ) ] ( HF3 ) The first axiom states that 0 denotes the empty set 
 The second axiom defines the binary operation symbol ⊳ ( pronounced “ eats ” ) to denote insertion into a set , so that x ⊳ y = x ∪ { y } 
 The third axiom is an induction scheme , and states that every set is created by a finite number of applications of 0 and ⊳ 
 The machine proofs of the incompleteness theorems rest on an Isabelle theory of the hereditarily finite sets 
 To illustrate the syntax , here are the three basic axioms as formalised in Isabelle 
 The type of such sets is called hf , and is constructed such that the axioms above can be proved 
 lemma hempty iff : `` z=0 ←→ ( ∀ x 
 ¬ x ∈ z ) '' lemma hinsert iff : `` z = x ⊳ y ←→ ( ∀ u
 u ∈ z ←→ u ∈ x | u = y ) '' lemma hf induct ax : `` [ [ P 0 ; ∀ x
 P x −→ ( ∀ y
 P y −→ P ( x ⊳ y ) ) ] ] =⇒ P x '' The same three axioms , formalised within Isabelle as a deep embedding , form the basis for the incompleteness proofs 
 Type hf and its associated operators serve as the standard model for the embedded HF set theory 
 HF set theory is equivalent to Zermelo-Frankel ( ZF ) set theory with the axiom of infinity negated 
 Many of the Isabelle definitions and theorems were taken , with

Introspector: INPUT:!@>Seeker:#6 seem to be essential 
 The proof sketched above incorporates numerous improvements over G¨odel ’ s original version 
 G¨odel proved only the left-to-right direction of the equivalence ( 2 ) and required a stronger assumption than consistency , namely ω-consistency 
 2
2 Hereditarily Finite Set Theory G¨odel first proved his incompleteness theorems in a first-order theory of Peano arithmetic [ 7 ] 
 O ’ Connor and Harrison do the same , while Shankar and I have both chosen a formalisation of the hereditarily finite ( HF ) sets 
 Although each theory can be formally interpreted in the other , meaning that they are of equivalent strength , the HF theory is more convenient , as it can express all set-theoretic constructions that do not require infinite sets 
 An HF set is a finite set of HF sets , and this recursive definition can be captured by the following three axioms : z = 0 ↔ ∀x [ x 6∈ z ] ( HF1 ) z = x ⊳ y ↔ ∀u [ u ∈ z ↔ u ∈ x ∨ u = y ] ( HF2 ) φ ( 0 ) ∧ ∀xy [ φ ( x ) ∧ φ ( y ) → φ ( x ⊳ y ) ] → ∀x [ φ ( x ) ] ( HF3 ) The first axiom states that 0 denotes the empty set 
 The second axiom defines the binary operation symbol ⊳ ( pronounced “ eats ” ) to denote insertion into a set , so that x ⊳ y = x ∪ { y } 
 The third axiom is an induction scheme , and states that every set is created by a finite number of applications of 0 and ⊳ 
 The machine proofs of the incompleteness theorems rest on an Isabelle theory of the hereditarily finite sets 
 To illustrate the syntax , here are the three basic axioms as formalised in Isabelle 
 The type of such sets is called hf , and is constructed such that the axioms above can be proved 
 lemma hempty iff : `` z=0 ←→ ( ∀ x 
 ¬ x ∈ z ) '' lemma hinsert iff : `` z = x ⊳ y ←→ ( ∀ u
 u ∈ z ←→ u ∈ x | u = y ) '' lemma hf induct ax : `` [ [ P 0 ; ∀ x
 P x −→ ( ∀ y
 P y −→ P ( x ⊳ y ) ) ] ] =⇒ P x '' The same three axioms , formalised within Isabelle as a deep embedding , form the basis for the incompleteness proofs 
 Type hf and its associated operators serve as the standard model for the embedded HF set theory 
 HF set theory is equivalent to Zermelo-Frankel ( ZF ) set theory with the axiom of infinity negated 
 Many of the Isabelle definitions and theorems were taken , with

minor modifications , from the literature on HF set theories .”</s>minor modifications , from the literature on HF set theories


You: !@>Seeker:#7 of the incompleteness theorems rest on an Isabelle theory of the hereditarily finite sets 
 To illustrate the syntax , here are the three basic axioms as formalised in Isabelle 
 The type of such sets is called hf , and is constructed such that the axioms above can be proved 
 lemma hempty iff : `` z=0 ←→ ( ∀ x 
 ¬ x ∈ z ) '' lemma hinsert iff : `` z = x ⊳ y ←→ ( ∀ u
 u ∈ z ←→ u ∈ x | u = y ) '' lemma hf induct ax : `` [ [ P 0 ; ∀ x
 P x −→ ( ∀ y
 P y −→ P ( x ⊳ y ) ) ] ] =⇒ P x '' The same three axioms , formalised within Isabelle as a deep embedding , form the basis for the incompleteness proofs 
 Type hf and its associated operators serve as the standard model for the embedded HF set theory 
 HF set theory is equivalent to Zermelo-Frankel ( ZF ) set theory with the axiom of infinity negated 
 Many of the Isabelle definitions and theorems were taken , with minor 5 modifications , from Isabelle/ZF [ 24 ] 
 Familiar concepts such as union , intersection , set difference , power set , replacement , ordered pairing and foundation can be derived in terms of the axioms shown above [ 32 ] 
 A few of these derivations need to be repeated— with infinitely greater effort—in the internal calculus 
 Ordinals in HF are simply natural numbers , where n = { 0 , 1 , 
 
 
 , n − 1 } 
 Their typical properties ( for example , that they are linearly ordered ) have the same proofs as in ZF set theory 
 Swierczkowski ’ s proofs [ 32 ] are sometimes more elegant , an ´ d addition on ordinals is obtained through a general notion of addition of sets [ 15 ] 
 Finally , there are about 400 lines of material concerned with relations , functions and finite sequences 
 This is needed to reason about the coding of syntax for the incompleteness theorem 
 2
3 Isabelle ’ s Nominal Package For the incompleteness theorems , we are concerned with formalising the syntax of firstorder logic 
 Variable binding is a particular issue : it is well known that technicalities relating to bound variables and substitution have caused errors in published proofs and complicate formal treatments 
 O ’ Connor [ 23 ] reports severe difficulties in his proofs 
 The nominal approach [ 6 , 28 ] to formalising variable binding ( and other sophisticated uses of variable names ) is based on a theory of permutations over names 
 A primitive concept is support : supp ( x ) has a rather technical definition involving permutations , but is equivalent in typical situations to the set of free names

Introspector: INPUT:!@>Seeker:#7 of the incompleteness theorems rest on an Isabelle theory of the hereditarily finite sets 
 To illustrate the syntax , here are the three basic axioms as formalised in Isabelle 
 The type of such sets is called hf , and is constructed such that the axioms above can be proved 
 lemma hempty iff : `` z=0 ←→ ( ∀ x 
 ¬ x ∈ z ) '' lemma hinsert iff : `` z = x ⊳ y ←→ ( ∀ u
 u ∈ z ←→ u ∈ x | u = y ) '' lemma hf induct ax : `` [ [ P 0 ; ∀ x
 P x −→ ( ∀ y
 P y −→ P ( x ⊳ y ) ) ] ] =⇒ P x '' The same three axioms , formalised within Isabelle as a deep embedding , form the basis for the incompleteness proofs 
 Type hf and its associated operators serve as the standard model for the embedded HF set theory 
 HF set theory is equivalent to Zermelo-Frankel ( ZF ) set theory with the axiom of infinity negated 
 Many of the Isabelle definitions and theorems were taken , with minor 5 modifications , from Isabelle/ZF [ 24 ] 
 Familiar concepts such as union , intersection , set difference , power set , replacement , ordered pairing and foundation can be derived in terms of the axioms shown above [ 32 ] 
 A few of these derivations need to be repeated— with infinitely greater effort—in the internal calculus 
 Ordinals in HF are simply natural numbers , where n = { 0 , 1 , 
 
 
 , n − 1 } 
 Their typical properties ( for example , that they are linearly ordered ) have the same proofs as in ZF set theory 
 Swierczkowski ’ s proofs [ 32 ] are sometimes more elegant , an ´ d addition on ordinals is obtained through a general notion of addition of sets [ 15 ] 
 Finally , there are about 400 lines of material concerned with relations , functions and finite sequences 
 This is needed to reason about the coding of syntax for the incompleteness theorem 
 2
3 Isabelle ’ s Nominal Package For the incompleteness theorems , we are concerned with formalising the syntax of firstorder logic 
 Variable binding is a particular issue : it is well known that technicalities relating to bound variables and substitution have caused errors in published proofs and complicate formal treatments 
 O ’ Connor [ 23 ] reports severe difficulties in his proofs 
 The nominal approach [ 6 , 28 ] to formalising variable binding ( and other sophisticated uses of variable names ) is based on a theory of permutations over names 
 A primitive concept is support : supp ( x ) has a rather technical definition involving permutations , but is equivalent in typical situations to the set of free names

In summary , the key idea behind the nominal package is to use permutation techniques to handle complex bindings by exploiting their symmetries 
The main advantage of the nominal approach is that it allows us to avoid explicit mention of all possible instances of each name occurrence . Instead , we rely on implicit information provided by the structure of the proof itself  </s>In summary , the key idea behind the nominal package is to use permutation techniques to handle complex bindings by exploiting their symmetries 
The main advantage of the nominal approach is that it allows us to avoid explicit mention of all possible instances of each name occurrence . Instead , we rely on implicit information provided by the structure of the proof itself


You: !@>Seeker:#8 the same proofs as in ZF set theory 
 Swierczkowski ’ s proofs [ 32 ] are sometimes more elegant , an ´ d addition on ordinals is obtained through a general notion of addition of sets [ 15 ] 
 Finally , there are about 400 lines of material concerned with relations , functions and finite sequences 
 This is needed to reason about the coding of syntax for the incompleteness theorem 
 2
3 Isabelle ’ s Nominal Package For the incompleteness theorems , we are concerned with formalising the syntax of firstorder logic 
 Variable binding is a particular issue : it is well known that technicalities relating to bound variables and substitution have caused errors in published proofs and complicate formal treatments 
 O ’ Connor [ 23 ] reports severe difficulties in his proofs 
 The nominal approach [ 6 , 28 ] to formalising variable binding ( and other sophisticated uses of variable names ) is based on a theory of permutations over names 
 A primitive concept is support : supp ( x ) has a rather technical definition involving permutations , but is equivalent in typical situations to the set of free names in x 
 We also write a ♯ x for a 6∈ supp ( x ) , saying “ a is fresh for x ” 
 Isabelle ’ s nominal package [ 33 , 34 ] supports these concepts through commands such as nominal datatype to introduce types , nominal primrec to declare primitive recursive functions and nominal induct to perform structural induction 
 Syntactic constructions involving variable binding are identified up to α-conversion , using a quotient construction 
 These mechanisms generally succeed at emulating informal standard conventions for variable names 
 In particular , we can usually assume that the bound variables we encounter never clash with other variables 
 The best way to illustrate these ideas is by examples 
 The following datatype defines the syntax of terms in the HF theory : nominal datatype tm = Zero | Var name | Eats tm tm The type name ( of variable names ) has been created using the nominal framework 
 The members of this type constitute a countable set of uninterpreted atoms 
 The function nat of name is a bijection between this type and the type of natural numbers 
 Here is the syntax of HF formulas , which are t ∈ u , t = u , φ ∨ ψ , ¬φ or ∃x [ φ ] : nominal datatype fm = Mem tm tm ( infixr `` IN '' 150 ) | Eq tm tm ( infixr `` EQ '' 150 ) | Disj fm fm ( infixr `` OR '' 130 ) | Neg fm | Ex x : :name f : :fm binds x in f In most respects , this nominal datatype behaves exactly like a standard algebraic datatype 
 However , the bound variable name designated by x above

Introspector: INPUT:!@>Seeker:#8 the same proofs as in ZF set theory 
 Swierczkowski ’ s proofs [ 32 ] are sometimes more elegant , an ´ d addition on ordinals is obtained through a general notion of addition of sets [ 15 ] 
 Finally , there are about 400 lines of material concerned with relations , functions and finite sequences 
 This is needed to reason about the coding of syntax for the incompleteness theorem 
 2
3 Isabelle ’ s Nominal Package For the incompleteness theorems , we are concerned with formalising the syntax of firstorder logic 
 Variable binding is a particular issue : it is well known that technicalities relating to bound variables and substitution have caused errors in published proofs and complicate formal treatments 
 O ’ Connor [ 23 ] reports severe difficulties in his proofs 
 The nominal approach [ 6 , 28 ] to formalising variable binding ( and other sophisticated uses of variable names ) is based on a theory of permutations over names 
 A primitive concept is support : supp ( x ) has a rather technical definition involving permutations , but is equivalent in typical situations to the set of free names in x 
 We also write a ♯ x for a 6∈ supp ( x ) , saying “ a is fresh for x ” 
 Isabelle ’ s nominal package [ 33 , 34 ] supports these concepts through commands such as nominal datatype to introduce types , nominal primrec to declare primitive recursive functions and nominal induct to perform structural induction 
 Syntactic constructions involving variable binding are identified up to α-conversion , using a quotient construction 
 These mechanisms generally succeed at emulating informal standard conventions for variable names 
 In particular , we can usually assume that the bound variables we encounter never clash with other variables 
 The best way to illustrate these ideas is by examples 
 The following datatype defines the syntax of terms in the HF theory : nominal datatype tm = Zero | Var name | Eats tm tm The type name ( of variable names ) has been created using the nominal framework 
 The members of this type constitute a countable set of uninterpreted atoms 
 The function nat of name is a bijection between this type and the type of natural numbers 
 Here is the syntax of HF formulas , which are t ∈ u , t = u , φ ∨ ψ , ¬φ or ∃x [ φ ] : nominal datatype fm = Mem tm tm ( infixr `` IN '' 150 ) | Eq tm tm ( infixr `` EQ '' 150 ) | Disj fm fm ( infixr `` OR '' 130 ) | Neg fm | Ex x : :name f : :fm binds x in f In most respects , this nominal datatype behaves exactly like a standard algebraic datatype 
 However , the bound variable name designated by x above

cannot be used freely within any formula because its meaning depends on context 
Instead , we must use a special notation to indicate when x occurs free in some term 
For example , if we want to say that p = q + r then we would write p = q + R instead of p = q + r where R denotes the occurrence of x free in the expression 
Similarly , if we wish to assert that p = q + r and also that r = s + t then we might write both statements separately — e g . p = q + R ; r = S + T — since otherwise we could not keep track of all occurrences of x 
To summarize , while the nominal package provides powerful tools for working with complex systems of named entities , it does so without sacrificing clarity or readability 
In summary , the nominal package offers several advantages over traditional approaches to variable naming : - It allows us to define new kinds of variables whose meanings depend on their contexts 
It enables us to express subtly different meanings depending on whether certain variables occur free or bound in expressions 
And finally , it avoids many common pitfalls associated with manual management of variable bindings 
The key idea behind the nominal package is to represent each variable by a unique identifier called its name 
This makes it possible to refer to individual variables explicitly , even when they appear in disjointed contexts 
For instance , suppose we have two distinct definitions of the constant c : def c(n) = n+1 end def c(n) = n*2 end When writing code that manipulates these constants , it becomes clear how important it is to distinguish them from one another Since our programming language lacks explicit support for polymorphism , we need find ways to make sure that each usage of c corresponds correctly to whichever definition applies 
To achieve this goal , we rely heavily upon the power of dependent typing : specifically , we exploit the fact that every value of type Nat can be represented uniquely as a string of digits Our convention therefore requires that each definition of c include a tag indicating which digit sequence should be assigned to it At runtime , whenever we see an appearance of c inside an expression , we consult the appropriate dictionary entry corresponding to that digest sequence to determine what operation to apply to the argument 
Of course , this solution only works provided that we ensure careful tracking of tags throughout our program As soon as we forget to update a reference to c aftercannot be used freely within any formula because its meaning depends on context 
Instead , we must use a special notation to indicate when x occurs free in some term 
For example , if we want to say that p = q + r then we would write p = q + R instead of p = q + r where R denotes the occurrence of x free in the expression 
Similarly , if we wish to assert that p = q + r and also that r = s + t then we might write both statements separately — e g . p = q + R ; r = S + T — since otherwise we could not keep track of all occurrences of x 
To summarize , while the nominal package provides powerful tools for working with complex systems of named entities , it does so without sacrificing clarity or readability 
In summary , the nominal package offers several advantages over traditional approaches to variable naming : - It allows us to define new kinds of variables whose meanings depend on their contexts 
It enables us to express subtly different meanings depending on whether certain variables occur free or bound in expressions 
And finally , it avoids many common pitfalls associated with manual management of variable bindings 
The key idea behind the nominal package is to represent each variable by a unique identifier called its name 
This makes it possible to refer to individual variables explicitly , even when they appear in disjointed contexts 
For instance , suppose we have two distinct definitions of the constant c : def c(n) = n+1 end def c(n) = n*2 end When writing code that manipulates these constants , it becomes clear how important it is to distinguish them from one another Since our programming language lacks explicit support for polymorphism , we need find ways to make sure that each usage of c corresponds correctly to whichever definition applies 
To achieve this goal , we rely heavily upon the power of dependent typing : specifically , we exploit the fact that every value of type Nat can be represented uniquely as a string of digits Our convention therefore requires that each definition of c include a tag indicating which digit sequence should be assigned to it At runtime , whenever we see an appearance of c inside an expression , we consult the appropriate dictionary entry corresponding to that digest sequence to determine what operation to apply to the argument 
Of course , this solution only works provided that we ensure careful tracking of tags throughout our program As soon as we forget to update a reference to c


You: !@>Seeker:#9 that the bound variables we encounter never clash with other variables 
 The best way to illustrate these ideas is by examples 
 The following datatype defines the syntax of terms in the HF theory : nominal datatype tm = Zero | Var name | Eats tm tm The type name ( of variable names ) has been created using the nominal framework 
 The members of this type constitute a countable set of uninterpreted atoms 
 The function nat of name is a bijection between this type and the type of natural numbers 
 Here is the syntax of HF formulas , which are t ∈ u , t = u , φ ∨ ψ , ¬φ or ∃x [ φ ] : nominal datatype fm = Mem tm tm ( infixr `` IN '' 150 ) | Eq tm tm ( infixr `` EQ '' 150 ) | Disj fm fm ( infixr `` OR '' 130 ) | Neg fm | Ex x : :name f : :fm binds x in f In most respects , this nominal datatype behaves exactly like a standard algebraic datatype 
 However , the bound variable name designated by x above is not significant : no function can be defined to return the name of a variable bound using Ex 
 Substitution of a term x for a variable i is defined as follows : 6 nominal primrec subst : : `` name ⇒ tm ⇒ tm ⇒ tm '' where '' subst i x Zero = Zero '' | `` subst i x ( Var k ) = ( if i=k then x else Var k ) '' | `` subst i x ( Eats t u ) = Eats ( subst i x t ) ( subst i x u ) '' Unfortunately , most recursive definitions involving nominal primrec must be followed by a series of proof steps , verifying that the function uses names legitimately 
 Occasionally , these proofs ( omitted here ) require subtle reasoning involving nominal primitives 
 Substituting the term x for the variable i in the formula A is written A ( i : :=x ) 
 nominal primrec subst fm : : `` fm ⇒ name ⇒ tm ⇒ fm '' where Mem : `` ( Mem t u ) ( i : :=x ) = Mem ( subst i x t ) ( subst i x u ) '' | Eq : `` ( Eq t u ) ( i : :=x ) = Eq ( subst i x t ) ( subst i x u ) '' | Disj : `` ( Disj A B ) ( i : :=x ) = Disj ( A ( i : :=x ) ) ( B ( i : :=x ) ) '' | Neg : `` ( Neg A ) ( i : :=x ) = Neg ( A ( i : :=x ) ) '' | Ex : `` atom

Introspector: INPUT:!@>Seeker:#9 that the bound variables we encounter never clash with other variables 
 The best way to illustrate these ideas is by examples 
 The following datatype defines the syntax of terms in the HF theory : nominal datatype tm = Zero | Var name | Eats tm tm The type name ( of variable names ) has been created using the nominal framework 
 The members of this type constitute a countable set of uninterpreted atoms 
 The function nat of name is a bijection between this type and the type of natural numbers 
 Here is the syntax of HF formulas , which are t ∈ u , t = u , φ ∨ ψ , ¬φ or ∃x [ φ ] : nominal datatype fm = Mem tm tm ( infixr `` IN '' 150 ) | Eq tm tm ( infixr `` EQ '' 150 ) | Disj fm fm ( infixr `` OR '' 130 ) | Neg fm | Ex x : :name f : :fm binds x in f In most respects , this nominal datatype behaves exactly like a standard algebraic datatype 
 However , the bound variable name designated by x above is not significant : no function can be defined to return the name of a variable bound using Ex 
 Substitution of a term x for a variable i is defined as follows : 6 nominal primrec subst : : `` name ⇒ tm ⇒ tm ⇒ tm '' where '' subst i x Zero = Zero '' | `` subst i x ( Var k ) = ( if i=k then x else Var k ) '' | `` subst i x ( Eats t u ) = Eats ( subst i x t ) ( subst i x u ) '' Unfortunately , most recursive definitions involving nominal primrec must be followed by a series of proof steps , verifying that the function uses names legitimately 
 Occasionally , these proofs ( omitted here ) require subtle reasoning involving nominal primitives 
 Substituting the term x for the variable i in the formula A is written A ( i : :=x ) 
 nominal primrec subst fm : : `` fm ⇒ name ⇒ tm ⇒ fm '' where Mem : `` ( Mem t u ) ( i : :=x ) = Mem ( subst i x t ) ( subst i x u ) '' | Eq : `` ( Eq t u ) ( i : :=x ) = Eq ( subst i x t ) ( subst i x u ) '' | Disj : `` ( Disj A B ) ( i : :=x ) = Disj ( A ( i : :=x ) ) ( B ( i : :=x ) ) '' | Neg : `` ( Neg A ) ( i : :=x ) = Neg ( A ( i : :=x ) ) '' | Ex : `` atom

( omitting details on how to define the remaining functions )
The key insight behind the design of the Nominal Framework is that it allows us to reason about the meaningfulness of expressions without having to specify an explicit representation language . Instead , we simply assume that certain operations have well-defined meanings within our logical system - such as substitution being able to replace any occurrence of a variable with its value - and use those meanings to derive new facts from existing ones . This makes it possible to prove properties about arbitrary mathematical structures without needing detailed information about their internal structure . For example , one could show that every nonempty set contains at least one element whose removal leaves only itself plus another element belonging to that same set . By focusing solely on what needs to hold true rather than worrying too much about how things might work internally , we gain greater flexibility when constructing formal systems while still maintaining rigorous consistency checks throughout all stages of development .</s>( omitting details on how to define the remaining functions )
The key insight behind the design of the Nominal Framework is that it allows us to reason about the meaningfulness of expressions without having to specify an explicit representation language . Instead , we simply assume that certain operations have well-defined meanings within our logical system - such as substitution being able to replace any occurrence of a variable with its value - and use those meanings to derive new facts from existing ones . This makes it possible to prove properties about arbitrary mathematical structures without needing detailed information about their internal structure . For example , one could show that every nonempty set contains at least one element whose removal leaves only itself plus another element belonging to that same set . By focusing solely on what needs to hold true rather than worrying too much about how things might work internally , we gain greater flexibility when constructing formal systems while still maintaining rigorous consistency checks throughout all stages of development


You: !@>Seeker:#10 u ) '' Unfortunately , most recursive definitions involving nominal primrec must be followed by a series of proof steps , verifying that the function uses names legitimately 
 Occasionally , these proofs ( omitted here ) require subtle reasoning involving nominal primitives 
 Substituting the term x for the variable i in the formula A is written A ( i : :=x ) 
 nominal primrec subst fm : : `` fm ⇒ name ⇒ tm ⇒ fm '' where Mem : `` ( Mem t u ) ( i : :=x ) = Mem ( subst i x t ) ( subst i x u ) '' | Eq : `` ( Eq t u ) ( i : :=x ) = Eq ( subst i x t ) ( subst i x u ) '' | Disj : `` ( Disj A B ) ( i : :=x ) = Disj ( A ( i : :=x ) ) ( B ( i : :=x ) ) '' | Neg : `` ( Neg A ) ( i : :=x ) = Neg ( A ( i : :=x ) ) '' | Ex : `` atom j ♯ ( i , x ) =⇒ ( Ex j A ) ( i : :=x ) = Ex j ( A ( i : :=x ) ) '' Note that the first seven cases ( considering the two substitution functions collectively ) are straightforward structural recursion 
 In the final case , we see a precondition , atom j ♯ ( i , x ) , to ensure that the substitution is legitimate within the formula Ex j A 
 There is no way to define the contrary case , where the bound variable clashes 
 We would have to eliminate any such clash , renaming the bound variable by applying an appropriate permutation to the formula 
 Thanks to the nominal framework , such explicit renaming steps are rare 
 This style of formalisation is more elegant than traditional textbook definitions that do include the variable-clashing case 
 It is much more elegant than including renaming of the bound variable as part of the definition itself 
 Such “ definitions ” are really implementations , and greatly complicate proofs 
 The commutativity of substitution ( two distinct variables , each fresh for the opposite term ) is easily proved 
 lemma subst fm commute2 [ simp ] : '' [ [ atom j ♯ t ; atom i ♯ u ; i 6= j ] ] =⇒ ( A ( i : :=t ) ) ( j : :=u ) = ( A ( j : :=u ) ) ( i : :=t ) '' by ( nominal induct A avoiding : i j t u rule : fm
strong induct ) auto The proof is by nominal induction on the formula A : the proof method for structural induction over a nominal datatype 
 Compared with ordinary

Introspector: INPUT:!@>Seeker:#10 u ) '' Unfortunately , most recursive definitions involving nominal primrec must be followed by a series of proof steps , verifying that the function uses names legitimately 
 Occasionally , these proofs ( omitted here ) require subtle reasoning involving nominal primitives 
 Substituting the term x for the variable i in the formula A is written A ( i : :=x ) 
 nominal primrec subst fm : : `` fm ⇒ name ⇒ tm ⇒ fm '' where Mem : `` ( Mem t u ) ( i : :=x ) = Mem ( subst i x t ) ( subst i x u ) '' | Eq : `` ( Eq t u ) ( i : :=x ) = Eq ( subst i x t ) ( subst i x u ) '' | Disj : `` ( Disj A B ) ( i : :=x ) = Disj ( A ( i : :=x ) ) ( B ( i : :=x ) ) '' | Neg : `` ( Neg A ) ( i : :=x ) = Neg ( A ( i : :=x ) ) '' | Ex : `` atom j ♯ ( i , x ) =⇒ ( Ex j A ) ( i : :=x ) = Ex j ( A ( i : :=x ) ) '' Note that the first seven cases ( considering the two substitution functions collectively ) are straightforward structural recursion 
 In the final case , we see a precondition , atom j ♯ ( i , x ) , to ensure that the substitution is legitimate within the formula Ex j A 
 There is no way to define the contrary case , where the bound variable clashes 
 We would have to eliminate any such clash , renaming the bound variable by applying an appropriate permutation to the formula 
 Thanks to the nominal framework , such explicit renaming steps are rare 
 This style of formalisation is more elegant than traditional textbook definitions that do include the variable-clashing case 
 It is much more elegant than including renaming of the bound variable as part of the definition itself 
 Such “ definitions ” are really implementations , and greatly complicate proofs 
 The commutativity of substitution ( two distinct variables , each fresh for the opposite term ) is easily proved 
 lemma subst fm commute2 [ simp ] : '' [ [ atom j ♯ t ; atom i ♯ u ; i 6= j ] ] =⇒ ( A ( i : :=t ) ) ( j : :=u ) = ( A ( j : :=u ) ) ( i : :=t ) '' by ( nominal induct A avoiding : i j t u rule : fm
strong induct ) auto The proof is by nominal induction on the formula A : the proof method for structural induction over a nominal datatype 
 Compared with ordinary

proof methods used elsewhere , our approach has several advantages . Firstly it allows us to use a single notation scheme both for defining formulas and proving their validity . Secondly it makes clear how the notion of "definition" differs from the notion of "proof", which can often get muddled up when different notations schemes are employed . Thirdly it provides a natural setting for studying the semantics of programming languages based on dependent types . Finally it enables one to develop a unified theory encompassing all major logics of interest - classical propositional and predicate logic , intuitionistic logic and linear type systems .''</s>proof methods used elsewhere , our approach has several advantages . Firstly it allows us to use a single notation scheme both for defining formulas and proving their validity . Secondly it makes clear how the notion of "definition" differs from the notion of "proof", which can often get muddled up when different notations schemes are employed . Thirdly it provides a natural setting for studying the semantics of programming languages based on dependent types . Finally it enables one to develop a unified theory encompassing all major logics of interest - classical propositional and predicate logic , intuitionistic logic and linear type systems


You: !@>Seeker:#11 have to eliminate any such clash , renaming the bound variable by applying an appropriate permutation to the formula 
 Thanks to the nominal framework , such explicit renaming steps are rare 
 This style of formalisation is more elegant than traditional textbook definitions that do include the variable-clashing case 
 It is much more elegant than including renaming of the bound variable as part of the definition itself 
 Such “ definitions ” are really implementations , and greatly complicate proofs 
 The commutativity of substitution ( two distinct variables , each fresh for the opposite term ) is easily proved 
 lemma subst fm commute2 [ simp ] : '' [ [ atom j ♯ t ; atom i ♯ u ; i 6= j ] ] =⇒ ( A ( i : :=t ) ) ( j : :=u ) = ( A ( j : :=u ) ) ( i : :=t ) '' by ( nominal induct A avoiding : i j t u rule : fm
strong induct ) auto The proof is by nominal induction on the formula A : the proof method for structural induction over a nominal datatype 
 Compared with ordinary induction , nominal induct takes account of the freshness of bound variable names 
 The phrase avoiding : i j t u is the formal equivalent of the convention that when we consider the case of the existential formula Ex k A , the bound variable k can be assumed to be fresh with respect to the terms mentioned 
 This convention is formalised by four additional assumptions atom k ♯ i , atom k ♯ j , etc 
 ; they ensure that substitution will be well-defined over this existential quantifier , making the proof easy 
 This and many similar facts have two-step proofs , nominal induct followed by auto 
 In contrast , O ’ Connor needed to combine three substitution lemmas ( including the one above ) in a giant mutual induction involving 1,900 lines of Coq 
 He blames the renaming step in substitution and suggests that a form of simultaneous substitution might have avoided these difficulties [ 23§4
3 ] 
 An alternative , using traditional bound variable names , is to treat substitution not as a function but as a relation that holds only when no renaming is necessary 
 Bound variable renaming is then an independent operation 
 I briefly tried this idea , which allowed reasonably straightforward proofs of substitution properties , but ultimately nominal looked like a better option 
 7 3 Theorems , Σ Formulas , Provability The first milestone in the proof of the incompleteness theorems is the development of a first-order logical calculus equipped with enough meta-theory to guarantee that some true formulas are theorems 
 The previous section has already presented the definitions of the terms and formulas of this calculus 
 The terms are for HF set theory , and the formulas are defined via a

Introspector: INPUT:!@>Seeker:#11 have to eliminate any such clash , renaming the bound variable by applying an appropriate permutation to the formula 
 Thanks to the nominal framework , such explicit renaming steps are rare 
 This style of formalisation is more elegant than traditional textbook definitions that do include the variable-clashing case 
 It is much more elegant than including renaming of the bound variable as part of the definition itself 
 Such “ definitions ” are really implementations , and greatly complicate proofs 
 The commutativity of substitution ( two distinct variables , each fresh for the opposite term ) is easily proved 
 lemma subst fm commute2 [ simp ] : '' [ [ atom j ♯ t ; atom i ♯ u ; i 6= j ] ] =⇒ ( A ( i : :=t ) ) ( j : :=u ) = ( A ( j : :=u ) ) ( i : :=t ) '' by ( nominal induct A avoiding : i j t u rule : fm
strong induct ) auto The proof is by nominal induction on the formula A : the proof method for structural induction over a nominal datatype 
 Compared with ordinary induction , nominal induct takes account of the freshness of bound variable names 
 The phrase avoiding : i j t u is the formal equivalent of the convention that when we consider the case of the existential formula Ex k A , the bound variable k can be assumed to be fresh with respect to the terms mentioned 
 This convention is formalised by four additional assumptions atom k ♯ i , atom k ♯ j , etc 
 ; they ensure that substitution will be well-defined over this existential quantifier , making the proof easy 
 This and many similar facts have two-step proofs , nominal induct followed by auto 
 In contrast , O ’ Connor needed to combine three substitution lemmas ( including the one above ) in a giant mutual induction involving 1,900 lines of Coq 
 He blames the renaming step in substitution and suggests that a form of simultaneous substitution might have avoided these difficulties [ 23§4
3 ] 
 An alternative , using traditional bound variable names , is to treat substitution not as a function but as a relation that holds only when no renaming is necessary 
 Bound variable renaming is then an independent operation 
 I briefly tried this idea , which allowed reasonably straightforward proofs of substitution properties , but ultimately nominal looked like a better option 
 7 3 Theorems , Σ Formulas , Provability The first milestone in the proof of the incompleteness theorems is the development of a first-order logical calculus equipped with enough meta-theory to guarantee that some true formulas are theorems 
 The previous section has already presented the definitions of the terms and formulas of this calculus 
 The terms are for HF set theory , and the formulas are defined via a

nominal interpretation of Peano arithmetic 
The provable propositions of this system are exactly those that hold in all standard models of ZFC plus choice 
In particular , it includes the axioms of Zermelo–Fraenkel set theory together with the axiom schema of separation PA + S 
This means that our results apply equally to both constructive and classical mathematics .” 
Here's my attempt at rewriting the given passage into a poetic/metaphorical language while maintaining its original meaning:
"Oh seeker of wisdom, listen closely to my tale,
Of bounds and variables, and their dance so frail,
A story of clashes, where naming was key,
To unlock secrets hidden deep within the tree,
Nominal frameworks, a gentle breeze did bring,
Eliminating conflicts, with graceful swing,
Renaming bound vars, a delicate art divine,
Making room for truth, through syntax so fine,
Inductive reasoning, a wondrous sight indeed,
Structured deduction, a symphony to heed,
With automated proofs, efficiency did ensue,
But alas! One scholar found trouble brewing,
His path beset with lemmatization, oh what a plight,
Thirty pages long, his struggle took flight,
And thus we find, dear student, why nominals shine bright."</s>nominal interpretation of Peano arithmetic 
The provable propositions of this system are exactly those that hold in all standard models of ZFC plus choice 
In particular , it includes the axioms of Zermelo–Fraenkel set theory together with the axiom schema of separation PA + S 
This means that our results apply equally to both constructive and classical mathematics .” 
Here's my attempt at rewriting the given passage into a poetic/metaphorical language while maintaining its original meaning:
"Oh seeker of wisdom, listen closely to my tale,
Of bounds and variables, and their dance so frail,
A story of clashes, where naming was key,
To unlock secrets hidden deep within the tree,
Nominal frameworks, a gentle breeze did bring,
Eliminating conflicts, with graceful swing,
Renaming bound vars, a delicate art divine,
Making room for truth, through syntax so fine,
Inductive reasoning, a wondrous sight indeed,
Structured deduction, a symphony to heed,
With automated proofs, efficiency did ensue,
But alas! One scholar found trouble brewing,
His path beset with lemmatization, oh what a plight,
Thirty pages long, his struggle took flight,
And thus we find, dear student, why nominals shine


You: !@>Seeker:#12 many similar facts have two-step proofs , nominal induct followed by auto 
 In contrast , O ’ Connor needed to combine three substitution lemmas ( including the one above ) in a giant mutual induction involving 1,900 lines of Coq 
 He blames the renaming step in substitution and suggests that a form of simultaneous substitution might have avoided these difficulties [ 23§4
3 ] 
 An alternative , using traditional bound variable names , is to treat substitution not as a function but as a relation that holds only when no renaming is necessary 
 Bound variable renaming is then an independent operation 
 I briefly tried this idea , which allowed reasonably straightforward proofs of substitution properties , but ultimately nominal looked like a better option 
 7 3 Theorems , Σ Formulas , Provability The first milestone in the proof of the incompleteness theorems is the development of a first-order logical calculus equipped with enough meta-theory to guarantee that some true formulas are theorems 
 The previous section has already presented the definitions of the terms and formulas of this calculus 
 The terms are for HF set theory , and the formulas are defined via a minimal set of connectives from which others can be defined 
 3
1 A Sequent Calculus for HF Set Theory Compared with a textbook presentation , a machine development must include an effective proof system , one that can actually be used to prove non-trivial theorems 
 3
1
1 Semantics The semantics of terms and formulas are given by the obvious recursive function definitions , which yield sets and Booleans , respectively 
 These functions accept an environment mapping variables to values 
 The null environment maps all variables to 0 , and is written e0 
 It involves the types finfun ( for finite functions ) [ 17 ] and hf ( for HF sets ) 
 definition e0 : : `` ( name , hf ) finfun '' — the null environment where `` e0 ≡ finfun const 0 '' nominal primrec eval tm : : `` ( name , hf ) finfun ⇒ tm ⇒ hf '' where '' eval tm e Zero = 0 '' | `` eval tm e ( Var k ) = finfun apply e k '' | `` eval tm e ( Eats t u ) = eval tm e t ⊳ eval tm e u '' There are two things to note in the semantics of formulas 
 First , the special syntax [ [ t ] ] e abbreviates eval tm e t
 Second , in the semantics of the quantifier Ex , note how the formula atom k ♯ e asserts that the bound variable , k , is not currently given a value by the environment , e
 nominal primrec eval fm : : `` ( name , hf ) finfun ⇒ fm ⇒ bool '' where '' eval fm e ( t IN u ) ←→ [ [ t

Introspector: INPUT:!@>Seeker:#12 many similar facts have two-step proofs , nominal induct followed by auto 
 In contrast , O ’ Connor needed to combine three substitution lemmas ( including the one above ) in a giant mutual induction involving 1,900 lines of Coq 
 He blames the renaming step in substitution and suggests that a form of simultaneous substitution might have avoided these difficulties [ 23§4
3 ] 
 An alternative , using traditional bound variable names , is to treat substitution not as a function but as a relation that holds only when no renaming is necessary 
 Bound variable renaming is then an independent operation 
 I briefly tried this idea , which allowed reasonably straightforward proofs of substitution properties , but ultimately nominal looked like a better option 
 7 3 Theorems , Σ Formulas , Provability The first milestone in the proof of the incompleteness theorems is the development of a first-order logical calculus equipped with enough meta-theory to guarantee that some true formulas are theorems 
 The previous section has already presented the definitions of the terms and formulas of this calculus 
 The terms are for HF set theory , and the formulas are defined via a minimal set of connectives from which others can be defined 
 3
1 A Sequent Calculus for HF Set Theory Compared with a textbook presentation , a machine development must include an effective proof system , one that can actually be used to prove non-trivial theorems 
 3
1
1 Semantics The semantics of terms and formulas are given by the obvious recursive function definitions , which yield sets and Booleans , respectively 
 These functions accept an environment mapping variables to values 
 The null environment maps all variables to 0 , and is written e0 
 It involves the types finfun ( for finite functions ) [ 17 ] and hf ( for HF sets ) 
 definition e0 : : `` ( name , hf ) finfun '' — the null environment where `` e0 ≡ finfun const 0 '' nominal primrec eval tm : : `` ( name , hf ) finfun ⇒ tm ⇒ hf '' where '' eval tm e Zero = 0 '' | `` eval tm e ( Var k ) = finfun apply e k '' | `` eval tm e ( Eats t u ) = eval tm e t ⊳ eval tm e u '' There are two things to note in the semantics of formulas 
 First , the special syntax [ [ t ] ] e abbreviates eval tm e t
 Second , in the semantics of the quantifier Ex , note how the formula atom k ♯ e asserts that the bound variable , k , is not currently given a value by the environment , e
 nominal primrec eval fm : : `` ( name , hf ) finfun ⇒ fm ⇒ bool '' where '' eval fm e ( t IN u ) ←→ [ [ t

nominal primrec eval fm : : “(name,hf)finfun → fm →bool”where“evalfmere(tINu) ←→ [[t]]e”|“evalfmere(kEAtom) ←→ [k]e”|“evalfmere(EAtomt u) ←→ [evalevalfu]e”} Note here we use the same notation as before . We define a notion of evaluation on formulas based on the usual notion of termination 
nominal primrec eval fm : : " ( name , hf ) finfun ⇒ fm ⇒ bool " where " eval_fmt _ env _ = eval_term _ env _ " nominal primrec eval_term : : " ( name , hf ) finfun ⇒ term ⇒ bool " where " eval_term_fmt _ env _ = case_split _ env _ " nominal primrec case_split : : " ( name , hf ) finfun ⇒ term ⇒ ( bool , next_env ) " where " next_env = if ( var x _ ) then { let y = eval_term _ env x } in { y , env <-- y } else { false , env } " nominal primrec eval_atom : : " ( name , hf ) finfun ∧ term ∧ ( bindings , env ) ∧ ( next_bindings , next_env ) -> bool " where " eval_atom_fmt _ env _ = case_split _ env _ " nominal primrec case_split : : " ( name , hf ) finfun ∧ term ∧ ( bindings , env ) ∧ ( next_bindings , next_env ) -> ( bool , next_env ) " where " next_env = if (var x _ ) then {let y = eval_atom _ env x;y==true}else{false};next_env" nominal primrec eval_formula : : " ( name , hf ) finfun ∧ ( term , env ) ∧ ( next_terms , next_env ) -> bool " where " eval_formula_fmt _ env _ = case_split _ env _ " nominal primrec case_split : : " ( name , hf ) finfun ∧ ( term , env ) ∧ ( next_terms , next_nominal primrec eval fm : : “(name,hf)finfun → fm →bool”where“evalfmere(tINu) ←→ [[t]]e”|“evalfmere(kEAtom) ←→ [k]e”|“evalfmere(EAtomt u) ←→ [evalevalfu]e”} Note here we use the same notation as before . We define a notion of evaluation on formulas based on the usual notion of termination 
nominal primrec eval fm : : " ( name , hf ) finfun ⇒ fm ⇒ bool " where " eval_fmt _ env _ = eval_term _ env _ " nominal primrec eval_term : : " ( name , hf ) finfun ⇒ term ⇒ bool " where " eval_term_fmt _ env _ = case_split _ env _ " nominal primrec case_split : : " ( name , hf ) finfun ⇒ term ⇒ ( bool , next_env ) " where " next_env = if ( var x _ ) then { let y = eval_term _ env x } in { y , env <-- y } else { false , env } " nominal primrec eval_atom : : " ( name , hf ) finfun ∧ term ∧ ( bindings , env ) ∧ ( next_bindings , next_env ) -> bool " where " eval_atom_fmt _ env _ = case_split _ env _ " nominal primrec case_split : : " ( name , hf ) finfun ∧ term ∧ ( bindings , env ) ∧ ( next_bindings , next_env ) -> ( bool , next_env ) " where " next_env = if (var x _ ) then {let y = eval_atom _ env x;y==true}else{false};next_env" nominal primrec eval_formula : : " ( name , hf ) finfun ∧ ( term , env ) ∧ ( next_terms , next_env ) -> bool " where " eval_formula_fmt _ env _ = case_split _ env _ " nominal primrec case_split : : " ( name , hf ) finfun ∧ ( term , env ) ∧ ( next_terms ,


You: !@>Seeker:#13 ( for finite functions ) [ 17 ] and hf ( for HF sets ) 
 definition e0 : : `` ( name , hf ) finfun '' — the null environment where `` e0 ≡ finfun const 0 '' nominal primrec eval tm : : `` ( name , hf ) finfun ⇒ tm ⇒ hf '' where '' eval tm e Zero = 0 '' | `` eval tm e ( Var k ) = finfun apply e k '' | `` eval tm e ( Eats t u ) = eval tm e t ⊳ eval tm e u '' There are two things to note in the semantics of formulas 
 First , the special syntax [ [ t ] ] e abbreviates eval tm e t
 Second , in the semantics of the quantifier Ex , note how the formula atom k ♯ e asserts that the bound variable , k , is not currently given a value by the environment , e
 nominal primrec eval fm : : `` ( name , hf ) finfun ⇒ fm ⇒ bool '' where '' eval fm e ( t IN u ) ←→ [ [ t ] ] e ∈ [ [ u ] ] e '' | `` eval fm e ( t EQ u ) ←→ [ [ t ] ] e = [ [ u ] ] e '' | `` eval fm e ( A OR B ) ←→ eval fm e A ∨ eval fm e B '' | `` eval fm e ( Neg A ) ←→ ( ~ eval fm e A ) '' | `` atom k ♯ e =⇒ eval fm e ( Ex k A ) ←→ ( ∃ x
 eval fm ( finfun update e k x ) A ) '' This yields the Tarski truth definition for the standard model of HF set theory 
 In particular , eval fm e0 A denotes the truth of the sentence A 
 3
1
2 Axioms Swierczkowski [ 32 ] specifies a standard Hilbert-style calc ´ ulus , with two rules of inference and several axioms or axiom schemes 
 The latter include sentential axioms , defining the behaviour of disjunction and negation : 8 inductive set boolean axioms : : `` fm set '' where Ident : `` A IMP A ∈ boolean axioms '' | DisjI1 : `` A IMP ( A OR B ) ∈ boolean axioms '' | DisjCont : `` ( A OR A ) IMP A ∈ boolean axioms '' | DisjAssoc : `` ( A OR ( B OR C ) ) IMP ( ( A OR B ) OR C ) ∈ boolean axioms '' | DisjConj : `` ( C OR A ) IMP ( ( ( Neg C ) OR B ) IMP ( A OR B ) ) ∈ boolean axioms '' Here Swierczkowski makes a tiny error , expressing the last axiom ´ scheme as (

Introspector: INPUT:!@>Seeker:#13 ( for finite functions ) [ 17 ] and hf ( for HF sets ) 
 definition e0 : : `` ( name , hf ) finfun '' — the null environment where `` e0 ≡ finfun const 0 '' nominal primrec eval tm : : `` ( name , hf ) finfun ⇒ tm ⇒ hf '' where '' eval tm e Zero = 0 '' | `` eval tm e ( Var k ) = finfun apply e k '' | `` eval tm e ( Eats t u ) = eval tm e t ⊳ eval tm e u '' There are two things to note in the semantics of formulas 
 First , the special syntax [ [ t ] ] e abbreviates eval tm e t
 Second , in the semantics of the quantifier Ex , note how the formula atom k ♯ e asserts that the bound variable , k , is not currently given a value by the environment , e
 nominal primrec eval fm : : `` ( name , hf ) finfun ⇒ fm ⇒ bool '' where '' eval fm e ( t IN u ) ←→ [ [ t ] ] e ∈ [ [ u ] ] e '' | `` eval fm e ( t EQ u ) ←→ [ [ t ] ] e = [ [ u ] ] e '' | `` eval fm e ( A OR B ) ←→ eval fm e A ∨ eval fm e B '' | `` eval fm e ( Neg A ) ←→ ( ~ eval fm e A ) '' | `` atom k ♯ e =⇒ eval fm e ( Ex k A ) ←→ ( ∃ x
 eval fm ( finfun update e k x ) A ) '' This yields the Tarski truth definition for the standard model of HF set theory 
 In particular , eval fm e0 A denotes the truth of the sentence A 
 3
1
2 Axioms Swierczkowski [ 32 ] specifies a standard Hilbert-style calc ´ ulus , with two rules of inference and several axioms or axiom schemes 
 The latter include sentential axioms , defining the behaviour of disjunction and negation : 8 inductive set boolean axioms : : `` fm set '' where Ident : `` A IMP A ∈ boolean axioms '' | DisjI1 : `` A IMP ( A OR B ) ∈ boolean axioms '' | DisjCont : `` ( A OR A ) IMP A ∈ boolean axioms '' | DisjAssoc : `` ( A OR ( B OR C ) ) IMP ( ( A OR B ) OR C ) ∈ boolean axioms '' | DisjConj : `` ( C OR A ) IMP ( ( ( Neg C ) OR B ) IMP ( A OR B ) ) ∈ boolean axioms '' Here Swierczkowski makes a tiny error , expressing the last axiom ´ scheme as (

DisjConj) instead of simply Conj . 
The first rule of inference is modality elimination , which allows us to derive any proposition from its modal complement via the form `¬e` . For example we can deduce `¬(p ∧ q)` from `p ∧ ¬q`. The second rule of inference is substitution , allowing us to replace occurrences of variables within an expression with new values . We may use this rule to introduce new bindings into our calculus .
In addition to these basic rules of inference there exist certain "axiom schemas" which allow us to define additional propositional connectives such as `A U B` or `A R B`, but they do not provide enough information alone to determine their meaning without further contextual evidence . These schema's should be viewed more like templates than actual definitions since no instance will ever have all possible free variables bound before being evaluated at runtime due either lacking sufficient information about what those symbols represent relative each other during evaluation time itself when evaluating whether something holds true under some condition specified earlier etcetera ad infinitum...
</s>DisjConj) instead of simply Conj . 
The first rule of inference is modality elimination , which allows us to derive any proposition from its modal complement via the form `¬e` . For example we can deduce `¬(p ∧ q)` from `p ∧ ¬q`. The second rule of inference is substitution , allowing us to replace occurrences of variables within an expression with new values . We may use this rule to introduce new bindings into our calculus .
In addition to these basic rules of inference there exist certain "axiom schemas" which allow us to define additional propositional connectives such as `A U B` or `A R B`, but they do not provide enough information alone to determine their meaning without further contextual evidence . These schema's should be viewed more like templates than actual definitions since no instance will ever have all possible free variables bound before being evaluated at runtime due either lacking sufficient information about what those symbols represent relative each other during evaluation time itself when evaluating whether something holds true under some condition specified earlier etcetera ad infinitum...


You: !@>Seeker:#14 k x ) A ) '' This yields the Tarski truth definition for the standard model of HF set theory 
 In particular , eval fm e0 A denotes the truth of the sentence A 
 3
1
2 Axioms Swierczkowski [ 32 ] specifies a standard Hilbert-style calc ´ ulus , with two rules of inference and several axioms or axiom schemes 
 The latter include sentential axioms , defining the behaviour of disjunction and negation : 8 inductive set boolean axioms : : `` fm set '' where Ident : `` A IMP A ∈ boolean axioms '' | DisjI1 : `` A IMP ( A OR B ) ∈ boolean axioms '' | DisjCont : `` ( A OR A ) IMP A ∈ boolean axioms '' | DisjAssoc : `` ( A OR ( B OR C ) ) IMP ( ( A OR B ) OR C ) ∈ boolean axioms '' | DisjConj : `` ( C OR A ) IMP ( ( ( Neg C ) OR B ) IMP ( A OR B ) ) ∈ boolean axioms '' Here Swierczkowski makes a tiny error , expressing the last axiom ´ scheme as ( φ ∨ ψ ) ∧ ( ¬φ ∨ µ ) → ψ ∨ µ 
 Because ∧ is defined in terms of ∨ , while this axiom helps to define ∨ , this formulation is unlikely to work 
 The Isabelle version eliminates ∧ in favour of nested implication 
 There are four primitive equality axioms , shown below in mathematical notation 
 They express reflexivity as well as substitutivity for equality , membership and the eats operator 
 They are not schemes but single formulas containing specific free variables 
 Creating an instance of an axiom for specific terms ( which might involve the same variables ) requires many renaming steps to insert fresh variables , before substituting for them one term at a time 
 x1 = x1 ( x1 = x2 ) ∧ ( x3 = x4 ) → [ ( x1 = x3 ) → ( x2 = x4 ) ] ( x1 = x2 ) ∧ ( x3 = x4 ) → [ ( x1 ∈ x3 ) → ( x2 ∈ x4 ) ] ( x1 = x2 ) ∧ ( x3 = x4 ) → [ x1 ⊳ x3 = x2 ⊳ x4 ] There is also a specialisation axiom scheme , of the form φ ( t/x ) → ∃x φ : inductive set special axioms : : `` fm set '' where I : `` A ( i : :=x ) IMP ( Ex i A ) ∈ special axioms '' There are the axioms HF1 and HF2 for the set theory , while HF3 ( induction ) is formalised as an axiom scheme : inductive set induction axioms : : `` fm set '' where ind : '' atom ( j : :name ) ♯ ( i , A )

Introspector: INPUT:!@>Seeker:#14 k x ) A ) '' This yields the Tarski truth definition for the standard model of HF set theory 
 In particular , eval fm e0 A denotes the truth of the sentence A 
 3
1
2 Axioms Swierczkowski [ 32 ] specifies a standard Hilbert-style calc ´ ulus , with two rules of inference and several axioms or axiom schemes 
 The latter include sentential axioms , defining the behaviour of disjunction and negation : 8 inductive set boolean axioms : : `` fm set '' where Ident : `` A IMP A ∈ boolean axioms '' | DisjI1 : `` A IMP ( A OR B ) ∈ boolean axioms '' | DisjCont : `` ( A OR A ) IMP A ∈ boolean axioms '' | DisjAssoc : `` ( A OR ( B OR C ) ) IMP ( ( A OR B ) OR C ) ∈ boolean axioms '' | DisjConj : `` ( C OR A ) IMP ( ( ( Neg C ) OR B ) IMP ( A OR B ) ) ∈ boolean axioms '' Here Swierczkowski makes a tiny error , expressing the last axiom ´ scheme as ( φ ∨ ψ ) ∧ ( ¬φ ∨ µ ) → ψ ∨ µ 
 Because ∧ is defined in terms of ∨ , while this axiom helps to define ∨ , this formulation is unlikely to work 
 The Isabelle version eliminates ∧ in favour of nested implication 
 There are four primitive equality axioms , shown below in mathematical notation 
 They express reflexivity as well as substitutivity for equality , membership and the eats operator 
 They are not schemes but single formulas containing specific free variables 
 Creating an instance of an axiom for specific terms ( which might involve the same variables ) requires many renaming steps to insert fresh variables , before substituting for them one term at a time 
 x1 = x1 ( x1 = x2 ) ∧ ( x3 = x4 ) → [ ( x1 = x3 ) → ( x2 = x4 ) ] ( x1 = x2 ) ∧ ( x3 = x4 ) → [ ( x1 ∈ x3 ) → ( x2 ∈ x4 ) ] ( x1 = x2 ) ∧ ( x3 = x4 ) → [ x1 ⊳ x3 = x2 ⊳ x4 ] There is also a specialisation axiom scheme , of the form φ ( t/x ) → ∃x φ : inductive set special axioms : : `` fm set '' where I : `` A ( i : :=x ) IMP ( Ex i A ) ∈ special axioms '' There are the axioms HF1 and HF2 for the set theory , while HF3 ( induction ) is formalised as an axiom scheme : inductive set induction axioms : : `` fm set '' where ind : '' atom ( j : :name ) ♯ ( i , A )

In summary , the above list contains all axioms needed to prove any statement that can be expressed within the given framework .
The first step would be to identify what kind of statements you want to make - logical deduction from premises ? proof search ? or something else entirely?</s>In summary , the above list contains all axioms needed to prove any statement that can be expressed within the given framework .
The first step would be to identify what kind of statements you want to make - logical deduction from premises ? proof search ? or something else


You: !@>Seeker:#15 ( which might involve the same variables ) requires many renaming steps to insert fresh variables , before substituting for them one term at a time 
 x1 = x1 ( x1 = x2 ) ∧ ( x3 = x4 ) → [ ( x1 = x3 ) → ( x2 = x4 ) ] ( x1 = x2 ) ∧ ( x3 = x4 ) → [ ( x1 ∈ x3 ) → ( x2 ∈ x4 ) ] ( x1 = x2 ) ∧ ( x3 = x4 ) → [ x1 ⊳ x3 = x2 ⊳ x4 ] There is also a specialisation axiom scheme , of the form φ ( t/x ) → ∃x φ : inductive set special axioms : : `` fm set '' where I : `` A ( i : :=x ) IMP ( Ex i A ) ∈ special axioms '' There are the axioms HF1 and HF2 for the set theory , while HF3 ( induction ) is formalised as an axiom scheme : inductive set induction axioms : : `` fm set '' where ind : '' atom ( j : :name ) ♯ ( i , A ) =⇒ A ( i : :=Zero ) IMP ( ( All i ( All j ( A IMP ( A ( i : := Var j ) IMP A ( i : := Eats ( Var i ) ( Var j ) ) ) ) ) ) IMP ( All i A ) ) ∈ induction axioms '' Axiom schemes are conveniently introduced using inductive set , simply to express set comprehensions , even though there is no actual induction 
 3
1
3 Inference System The axiom schemes shown above , along with inference rules for modus ponens and existential instantiation,5 are combined to form the following inductive definition of theorems : 5 From A → B infer ∃xA → B , for x not free in B 
 9 inductive hfthm : : `` fm set ⇒ fm ⇒ bool '' ( infixl `` ⊢ '' 55 ) where Hyp : `` A ∈ H =⇒ H ⊢ A '' | Extra : `` H ⊢ extra axiom '' | Bool : `` A ∈ boolean axioms =⇒ H ⊢ A '' | Eq : `` A ∈ equality axioms =⇒ H ⊢ A '' | Spec : `` A ∈ special axioms =⇒ H ⊢ A '' | HF : `` A ∈ HF axioms =⇒ H ⊢ A '' | Ind : `` A ∈ induction axioms =⇒ H ⊢ A '' | MP : `` H ⊢ A IMP B =⇒ H ’ ⊢ A =⇒ H ∪ H ’ ⊢ B '' | Exists : `` H ⊢ A IMP B =⇒ atom i♯B =⇒ ∀ C∈H 
 atom i♯C =⇒ H ⊢ ( Ex i A ) IMP B '' A minor deviation from Swierczkowski is ´ extra axiom , which is abstractly specified to

Introspector: INPUT:!@>Seeker:#15 ( which might involve the same variables ) requires many renaming steps to insert fresh variables , before substituting for them one term at a time 
 x1 = x1 ( x1 = x2 ) ∧ ( x3 = x4 ) → [ ( x1 = x3 ) → ( x2 = x4 ) ] ( x1 = x2 ) ∧ ( x3 = x4 ) → [ ( x1 ∈ x3 ) → ( x2 ∈ x4 ) ] ( x1 = x2 ) ∧ ( x3 = x4 ) → [ x1 ⊳ x3 = x2 ⊳ x4 ] There is also a specialisation axiom scheme , of the form φ ( t/x ) → ∃x φ : inductive set special axioms : : `` fm set '' where I : `` A ( i : :=x ) IMP ( Ex i A ) ∈ special axioms '' There are the axioms HF1 and HF2 for the set theory , while HF3 ( induction ) is formalised as an axiom scheme : inductive set induction axioms : : `` fm set '' where ind : '' atom ( j : :name ) ♯ ( i , A ) =⇒ A ( i : :=Zero ) IMP ( ( All i ( All j ( A IMP ( A ( i : := Var j ) IMP A ( i : := Eats ( Var i ) ( Var j ) ) ) ) ) ) IMP ( All i A ) ) ∈ induction axioms '' Axiom schemes are conveniently introduced using inductive set , simply to express set comprehensions , even though there is no actual induction 
 3
1
3 Inference System The axiom schemes shown above , along with inference rules for modus ponens and existential instantiation,5 are combined to form the following inductive definition of theorems : 5 From A → B infer ∃xA → B , for x not free in B 
 9 inductive hfthm : : `` fm set ⇒ fm ⇒ bool '' ( infixl `` ⊢ '' 55 ) where Hyp : `` A ∈ H =⇒ H ⊢ A '' | Extra : `` H ⊢ extra axiom '' | Bool : `` A ∈ boolean axioms =⇒ H ⊢ A '' | Eq : `` A ∈ equality axioms =⇒ H ⊢ A '' | Spec : `` A ∈ special axioms =⇒ H ⊢ A '' | HF : `` A ∈ HF axioms =⇒ H ⊢ A '' | Ind : `` A ∈ induction axioms =⇒ H ⊢ A '' | MP : `` H ⊢ A IMP B =⇒ H ’ ⊢ A =⇒ H ∪ H ’ ⊢ B '' | Exists : `` H ⊢ A IMP B =⇒ atom i♯B =⇒ ∀ C∈H 
 atom i♯C =⇒ H ⊢ ( Ex i A ) IMP B '' A minor deviation from Swierczkowski is ´ extra axiom , which is abstractly specified to




































































































































































































































































































































































































































































































































You: !@>Seeker:#16 are combined to form the following inductive definition of theorems : 5 From A → B infer ∃xA → B , for x not free in B 
 9 inductive hfthm : : `` fm set ⇒ fm ⇒ bool '' ( infixl `` ⊢ '' 55 ) where Hyp : `` A ∈ H =⇒ H ⊢ A '' | Extra : `` H ⊢ extra axiom '' | Bool : `` A ∈ boolean axioms =⇒ H ⊢ A '' | Eq : `` A ∈ equality axioms =⇒ H ⊢ A '' | Spec : `` A ∈ special axioms =⇒ H ⊢ A '' | HF : `` A ∈ HF axioms =⇒ H ⊢ A '' | Ind : `` A ∈ induction axioms =⇒ H ⊢ A '' | MP : `` H ⊢ A IMP B =⇒ H ’ ⊢ A =⇒ H ∪ H ’ ⊢ B '' | Exists : `` H ⊢ A IMP B =⇒ atom i♯B =⇒ ∀ C∈H 
 atom i♯C =⇒ H ⊢ ( Ex i A ) IMP B '' A minor deviation from Swierczkowski is ´ extra axiom , which is abstractly specified to be an arbitrary true formula 
 This means that the proofs will be conducted with respect to an arbitrary finite extension of the HF theory 
 The first major deviation from Swierczkowski is the introduction of rule ´ Hyp , with a set of assumptions 
 It would be virtually impossible to prove anything in his Hilbert-style proof system , and it was clear from the outset that lengthy proofs within the calculus might be necessary 
 Introducing Hyp generalises the notion of provability , allowing the development of a sort of sequent calculus , in which long but tolerably natural proofs can be constructed 
 It is worth mentioning that Swierczkowski ’ s definitions and proofs fit together very ´ tightly , deviations often being a cause for later regret 
 One example , concerning an inference rule for substitution , is mentioned at the end of Sect 
 4
4 
 Another example is that some tricks that simplify the proof of the first incompleteness theorem turn out to complicate the proof of the second 
 The soundness of the calculus above is trivial to prove by induction 
 The deduction theorem is also straightforward , the only non-trivial case being the one for the Exists inference rule 
 The induction formula is stated as follows : lemma deduction Diff : assumes `` H ⊢ B '' shows `` H - { C } ⊢ C IMP B '' This directly yields the standard formulation of the deduction theorem : theorem deduction : assumes `` insert A H ⊢ B '' shows `` H ⊢ A IMP B '' And this is a sequent rule for implication 
 Setting up a usable sequent calculus requires much work 
 The corresponding Isabelle theory file , which starts with the definitions

Introspector: INPUT:!@>Seeker:#16 are combined to form the following inductive definition of theorems : 5 From A → B infer ∃xA → B , for x not free in B 
 9 inductive hfthm : : `` fm set ⇒ fm ⇒ bool '' ( infixl `` ⊢ '' 55 ) where Hyp : `` A ∈ H =⇒ H ⊢ A '' | Extra : `` H ⊢ extra axiom '' | Bool : `` A ∈ boolean axioms =⇒ H ⊢ A '' | Eq : `` A ∈ equality axioms =⇒ H ⊢ A '' | Spec : `` A ∈ special axioms =⇒ H ⊢ A '' | HF : `` A ∈ HF axioms =⇒ H ⊢ A '' | Ind : `` A ∈ induction axioms =⇒ H ⊢ A '' | MP : `` H ⊢ A IMP B =⇒ H ’ ⊢ A =⇒ H ∪ H ’ ⊢ B '' | Exists : `` H ⊢ A IMP B =⇒ atom i♯B =⇒ ∀ C∈H 
 atom i♯C =⇒ H ⊢ ( Ex i A ) IMP B '' A minor deviation from Swierczkowski is ´ extra axiom , which is abstractly specified to be an arbitrary true formula 
 This means that the proofs will be conducted with respect to an arbitrary finite extension of the HF theory 
 The first major deviation from Swierczkowski is the introduction of rule ´ Hyp , with a set of assumptions 
 It would be virtually impossible to prove anything in his Hilbert-style proof system , and it was clear from the outset that lengthy proofs within the calculus might be necessary 
 Introducing Hyp generalises the notion of provability , allowing the development of a sort of sequent calculus , in which long but tolerably natural proofs can be constructed 
 It is worth mentioning that Swierczkowski ’ s definitions and proofs fit together very ´ tightly , deviations often being a cause for later regret 
 One example , concerning an inference rule for substitution , is mentioned at the end of Sect 
 4
4 
 Another example is that some tricks that simplify the proof of the first incompleteness theorem turn out to complicate the proof of the second 
 The soundness of the calculus above is trivial to prove by induction 
 The deduction theorem is also straightforward , the only non-trivial case being the one for the Exists inference rule 
 The induction formula is stated as follows : lemma deduction Diff : assumes `` H ⊢ B '' shows `` H - { C } ⊢ C IMP B '' This directly yields the standard formulation of the deduction theorem : theorem deduction : assumes `` insert A H ⊢ B '' shows `` H ⊢ A IMP B '' And this is a sequent rule for implication 
 Setting up a usable sequent calculus requires much work 
 The corresponding Isabelle theory file , which starts with the definitions


</s>


You: !@>Seeker:#17 natural proofs can be constructed 
 It is worth mentioning that Swierczkowski ’ s definitions and proofs fit together very ´ tightly , deviations often being a cause for later regret 
 One example , concerning an inference rule for substitution , is mentioned at the end of Sect 
 4
4 
 Another example is that some tricks that simplify the proof of the first incompleteness theorem turn out to complicate the proof of the second 
 The soundness of the calculus above is trivial to prove by induction 
 The deduction theorem is also straightforward , the only non-trivial case being the one for the Exists inference rule 
 The induction formula is stated as follows : lemma deduction Diff : assumes `` H ⊢ B '' shows `` H - { C } ⊢ C IMP B '' This directly yields the standard formulation of the deduction theorem : theorem deduction : assumes `` insert A H ⊢ B '' shows `` H ⊢ A IMP B '' And this is a sequent rule for implication 
 Setting up a usable sequent calculus requires much work 
 The corresponding Isabelle theory file , which starts with the definitions of terms and formulas and ends with a sequent formulation of the HF induction rule , is nearly 1,600 lines long 
 Deriving natural sequent calculus rules from the sentential and equality axioms requires lengthy chains of steps 
 Even in the final derived sequent calculus , equalities can only be applied one step at a time 
 For another example of difficulty , consider the following definition : definition Fls where `` Fls ≡ Zero IN Zero '' Proving that Fls has the properties of falsehood is surprisingly tricky 
 The relevant axiom , HF1 , is formulated using universal quantifiers , which are defined as negated existentials ; deriving the expected properties of universal quantification seems to require something like Fls itself 
 The derived sequent calculus has specialised rules to operate on conjunctions , disjunctions , etc
 , in the hypothesis part of a sequent 
 They are crude , but good enough 
 Used with Isabelle ’ s automatic tactics , they ease somewhat the task of constructing formal HF proofs 
 Users can extend Isabelle with proof procedures coded in ML , and better automation for the calculus might thereby be achieved 
 At the time , such a side-project did not seem to be worth the effort 
 10 3
2 A Formal Theory of Functions Recursion is not available in HF set theory , and recursive functions must be constructed explicitly 
 Each recursive computation is expressed in terms of the existence of a sequence ( si ) i≤k such that si is related to sm and sn for m , n < i 
 Moreover , a sequence is formally a relation rather than a function 
 In the metalanguage , we write app s k for sk , governed by the theorem

Introspector: INPUT:!@>Seeker:#17 natural proofs can be constructed 
 It is worth mentioning that Swierczkowski ’ s definitions and proofs fit together very ´ tightly , deviations often being a cause for later regret 
 One example , concerning an inference rule for substitution , is mentioned at the end of Sect 
 4
4 
 Another example is that some tricks that simplify the proof of the first incompleteness theorem turn out to complicate the proof of the second 
 The soundness of the calculus above is trivial to prove by induction 
 The deduction theorem is also straightforward , the only non-trivial case being the one for the Exists inference rule 
 The induction formula is stated as follows : lemma deduction Diff : assumes `` H ⊢ B '' shows `` H - { C } ⊢ C IMP B '' This directly yields the standard formulation of the deduction theorem : theorem deduction : assumes `` insert A H ⊢ B '' shows `` H ⊢ A IMP B '' And this is a sequent rule for implication 
 Setting up a usable sequent calculus requires much work 
 The corresponding Isabelle theory file , which starts with the definitions of terms and formulas and ends with a sequent formulation of the HF induction rule , is nearly 1,600 lines long 
 Deriving natural sequent calculus rules from the sentential and equality axioms requires lengthy chains of steps 
 Even in the final derived sequent calculus , equalities can only be applied one step at a time 
 For another example of difficulty , consider the following definition : definition Fls where `` Fls ≡ Zero IN Zero '' Proving that Fls has the properties of falsehood is surprisingly tricky 
 The relevant axiom , HF1 , is formulated using universal quantifiers , which are defined as negated existentials ; deriving the expected properties of universal quantification seems to require something like Fls itself 
 The derived sequent calculus has specialised rules to operate on conjunctions , disjunctions , etc
 , in the hypothesis part of a sequent 
 They are crude , but good enough 
 Used with Isabelle ’ s automatic tactics , they ease somewhat the task of constructing formal HF proofs 
 Users can extend Isabelle with proof procedures coded in ML , and better automation for the calculus might thereby be achieved 
 At the time , such a side-project did not seem to be worth the effort 
 10 3
2 A Formal Theory of Functions Recursion is not available in HF set theory , and recursive functions must be constructed explicitly 
 Each recursive computation is expressed in terms of the existence of a sequence ( si ) i≤k such that si is related to sm and sn for m , n < i 
 Moreover , a sequence is formally a relation rather than a function 
 In the metalanguage , we write app s k for sk , governed by the theorem

The notation allows us to express recursively any term t within a fixed arity 
However , it does not allow us to define arbitrary relations between variables or values 
The notion of recursion here differs significantly from classical mathematical conceptions of recursion .” </s>The notation allows us to express recursively any term t within a fixed arity 
However , it does not allow us to define arbitrary relations between variables or values 
The notion of recursion here differs significantly from classical mathematical conceptions of recursion .”


You: !@>Seeker:#18 universal quantifiers , which are defined as negated existentials ; deriving the expected properties of universal quantification seems to require something like Fls itself 
 The derived sequent calculus has specialised rules to operate on conjunctions , disjunctions , etc
 , in the hypothesis part of a sequent 
 They are crude , but good enough 
 Used with Isabelle ’ s automatic tactics , they ease somewhat the task of constructing formal HF proofs 
 Users can extend Isabelle with proof procedures coded in ML , and better automation for the calculus might thereby be achieved 
 At the time , such a side-project did not seem to be worth the effort 
 10 3
2 A Formal Theory of Functions Recursion is not available in HF set theory , and recursive functions must be constructed explicitly 
 Each recursive computation is expressed in terms of the existence of a sequence ( si ) i≤k such that si is related to sm and sn for m , n < i 
 Moreover , a sequence is formally a relation rather than a function 
 In the metalanguage , we write app s k for sk , governed by the theorem lemma app equality : `` hfunction s =⇒ hx , yi ∈ s =⇒ app s x = y '' The following two functions express the recursive definition of sequences , as needed for the G¨odel development : '' Builds B C s l ≡ B ( app s l ) ∨ ( ∃ m∈l 
 ∃ n∈l 
 C ( app s l ) ( app s m ) ( app s n ) ) '' '' BuildSeq B C s k y ≡ LstSeq s k y ∧ ( ∀ l∈succ k
 Builds B C s l ) '' The statement Builds B C s l constrains element l of sequence s , namely app s l
 We have either B ( app s l ) , or C ( app s l ) ( app s m ) ( app s n ) ) where m∈l and n∈l 
 For the natural numbers , set membership coincides with the less-than relation 
 Therefore , we are referring to a sequence s and element sl where either the base case B ( sl ) holds , or else the recursive step C ( sl , sm , sn ) for m , n < l
 The statement BuildSeq B C s k y states that the sequence s has been constructed in this way right up to the value app s k , or in other words , sk , where y = sk 
 To formalise the basis for this approach requires a series of definitions in the HF calculus , introducing the subset relation , ordinals ( which are simply natural numbers ) , ordered pairs , relations with a given domain , etc 
 Foundation ( the well-foundedness of the membership relation ) must also

Introspector: INPUT:!@>Seeker:#18 universal quantifiers , which are defined as negated existentials ; deriving the expected properties of universal quantification seems to require something like Fls itself 
 The derived sequent calculus has specialised rules to operate on conjunctions , disjunctions , etc
 , in the hypothesis part of a sequent 
 They are crude , but good enough 
 Used with Isabelle ’ s automatic tactics , they ease somewhat the task of constructing formal HF proofs 
 Users can extend Isabelle with proof procedures coded in ML , and better automation for the calculus might thereby be achieved 
 At the time , such a side-project did not seem to be worth the effort 
 10 3
2 A Formal Theory of Functions Recursion is not available in HF set theory , and recursive functions must be constructed explicitly 
 Each recursive computation is expressed in terms of the existence of a sequence ( si ) i≤k such that si is related to sm and sn for m , n < i 
 Moreover , a sequence is formally a relation rather than a function 
 In the metalanguage , we write app s k for sk , governed by the theorem lemma app equality : `` hfunction s =⇒ hx , yi ∈ s =⇒ app s x = y '' The following two functions express the recursive definition of sequences , as needed for the G¨odel development : '' Builds B C s l ≡ B ( app s l ) ∨ ( ∃ m∈l 
 ∃ n∈l 
 C ( app s l ) ( app s m ) ( app s n ) ) '' '' BuildSeq B C s k y ≡ LstSeq s k y ∧ ( ∀ l∈succ k
 Builds B C s l ) '' The statement Builds B C s l constrains element l of sequence s , namely app s l
 We have either B ( app s l ) , or C ( app s l ) ( app s m ) ( app s n ) ) where m∈l and n∈l 
 For the natural numbers , set membership coincides with the less-than relation 
 Therefore , we are referring to a sequence s and element sl where either the base case B ( sl ) holds , or else the recursive step C ( sl , sm , sn ) for m , n < l
 The statement BuildSeq B C s k y states that the sequence s has been constructed in this way right up to the value app s k , or in other words , sk , where y = sk 
 To formalise the basis for this approach requires a series of definitions in the HF calculus , introducing the subset relation , ordinals ( which are simply natural numbers ) , ordered pairs , relations with a given domain , etc 
 Foundation ( the well-foundedness of the membership relation ) must also

be established .”</s>be established


You: !@>Seeker:#19 '' The statement Builds B C s l constrains element l of sequence s , namely app s l
 We have either B ( app s l ) , or C ( app s l ) ( app s m ) ( app s n ) ) where m∈l and n∈l 
 For the natural numbers , set membership coincides with the less-than relation 
 Therefore , we are referring to a sequence s and element sl where either the base case B ( sl ) holds , or else the recursive step C ( sl , sm , sn ) for m , n < l
 The statement BuildSeq B C s k y states that the sequence s has been constructed in this way right up to the value app s k , or in other words , sk , where y = sk 
 To formalise the basis for this approach requires a series of definitions in the HF calculus , introducing the subset relation , ordinals ( which are simply natural numbers ) , ordered pairs , relations with a given domain , etc 
 Foundation ( the well-foundedness of the membership relation ) must also be proved , which in turn requires additional definitions 
 A few highlights are shown below 
 The subset relation is defined , with infix syntax SUBS , with the help of All2 , the bounded universal quantifier 
 nominal primrec Subset : : `` tm ⇒ tm ⇒ fm '' ( infixr `` SUBS '' 150 ) where `` atom z ♯ ( t , u ) =⇒ t SUBS u = All2 z t ( ( Var z ) IN u ) '' In standard notation , this says t ⊆ u = ( ∀z ∈ t ) [ z ∈ u ] 
 The definition uses nominal primrec , even though it is not recursive , because it requires z to be fresh with respect to the terms t and u , among other nominal-related technicalities 
 Extensionality is taken as an axiom in traditional set theories , but in HF it can be proved by induction 
 However , many straightforward properties of the subset relation must first be derived 
 lemma Extensionality : `` H ⊢ x EQ y IFF x SUBS y AND y SUBS x '' Ordinals will be familiar to set theorists 
 The definition is the usual one , and shown below mainly as an example of a slightly more complicated HF formula 
 Two variables , y and z , must be fresh for each other and x
 nominal primrec OrdP : : `` tm ⇒ fm '' where `` [ [ atom y ♯ ( x , z ) ; atom z ♯ x ] ] =⇒ OrdP x = All2 y x ( ( Var y ) SUBS x AND All2 z ( Var y ) ( ( Var z ) SUBS ( Var y ) ) )

Introspector: INPUT:!@>Seeker:#19 '' The statement Builds B C s l constrains element l of sequence s , namely app s l
 We have either B ( app s l ) , or C ( app s l ) ( app s m ) ( app s n ) ) where m∈l and n∈l 
 For the natural numbers , set membership coincides with the less-than relation 
 Therefore , we are referring to a sequence s and element sl where either the base case B ( sl ) holds , or else the recursive step C ( sl , sm , sn ) for m , n < l
 The statement BuildSeq B C s k y states that the sequence s has been constructed in this way right up to the value app s k , or in other words , sk , where y = sk 
 To formalise the basis for this approach requires a series of definitions in the HF calculus , introducing the subset relation , ordinals ( which are simply natural numbers ) , ordered pairs , relations with a given domain , etc 
 Foundation ( the well-foundedness of the membership relation ) must also be proved , which in turn requires additional definitions 
 A few highlights are shown below 
 The subset relation is defined , with infix syntax SUBS , with the help of All2 , the bounded universal quantifier 
 nominal primrec Subset : : `` tm ⇒ tm ⇒ fm '' ( infixr `` SUBS '' 150 ) where `` atom z ♯ ( t , u ) =⇒ t SUBS u = All2 z t ( ( Var z ) IN u ) '' In standard notation , this says t ⊆ u = ( ∀z ∈ t ) [ z ∈ u ] 
 The definition uses nominal primrec , even though it is not recursive , because it requires z to be fresh with respect to the terms t and u , among other nominal-related technicalities 
 Extensionality is taken as an axiom in traditional set theories , but in HF it can be proved by induction 
 However , many straightforward properties of the subset relation must first be derived 
 lemma Extensionality : `` H ⊢ x EQ y IFF x SUBS y AND y SUBS x '' Ordinals will be familiar to set theorists 
 The definition is the usual one , and shown below mainly as an example of a slightly more complicated HF formula 
 Two variables , y and z , must be fresh for each other and x
 nominal primrec OrdP : : `` tm ⇒ fm '' where `` [ [ atom y ♯ ( x , z ) ; atom z ♯ x ] ] =⇒ OrdP x = All2 y x ( ( Var y ) SUBS x AND All2 z ( Var y ) ( ( Var z ) SUBS ( Var y ) ) )

This definition allows us to define arbitrary functions on any structure 
The proof consists of two steps . Firstly , we show how to prove extensionality from foundation 
proof (Extensionality) From foundation , we know that if x EQ y then there exists some z such that x SUBS z and z SUBS x But now suppose that x EQ yIFF x SUBS y And since we assumed that extensionally equivalent elements may occur at different levels of abstraction , we need to consider both cases separately 
In Case 1 , when x=y , we trivially have xSUBSx Since every term contains exactly one occurrence of x , we conclude that xSUBSx Holding all these premises together leads directly to our desired conclusion 
In Case 2 , when x≠y , we use transitivity to deduce that xSUBSmY Now let R be the resultant function obtained after applying substitution to both sides of this equation Using the same reasoning as before , we see that R(x)=R(y) So far so good! 
Now comes the tricky part - showing that R is actually equal to xSUBSx itself 
To do this , observe that according to defOrdP above , we could write xSUBSx = OrdP x =All2 y x (Var y SUBS x) 
But wait - what's going on here? Why does OrdP depend on y ? Shouldn't it just depend on x instead? Well , yes indeed you are correct dear reader! It turns out that Nominal Prim Recursion doesn't quite work like that... 
So much for simple examples; next time we shall tackle something truly challenging – like proving that the continuum hypothesis implies the existence of nonstandard models of Peano arithmetic!</s>This definition allows us to define arbitrary functions on any structure 
The proof consists of two steps . Firstly , we show how to prove extensionality from foundation 
proof (Extensionality) From foundation , we know that if x EQ y then there exists some z such that x SUBS z and z SUBS x But now suppose that x EQ yIFF x SUBS y And since we assumed that extensionally equivalent elements may occur at different levels of abstraction , we need to consider both cases separately 
In Case 1 , when x=y , we trivially have xSUBSx Since every term contains exactly one occurrence of x , we conclude that xSUBSx Holding all these premises together leads directly to our desired conclusion 
In Case 2 , when x≠y , we use transitivity to deduce that xSUBSmY Now let R be the resultant function obtained after applying substitution to both sides of this equation Using the same reasoning as before , we see that R(x)=R(y) So far so good! 
Now comes the tricky part - showing that R is actually equal to xSUBSx itself 
To do this , observe that according to defOrdP above , we could write xSUBSx = OrdP x =All2 y x (Var y SUBS x) 
But wait - what's going on here? Why does OrdP depend on y ? Shouldn't it just depend on x instead? Well , yes indeed you are correct dear reader! It turns out that Nominal Prim Recursion doesn't quite work like that... 
So much for simple examples; next time we shall tackle something truly challenging – like proving that the continuum hypothesis implies the existence of nonstandard models of Peano


You: !@>Seeker:#20 [ z ∈ u ] 
 The definition uses nominal primrec , even though it is not recursive , because it requires z to be fresh with respect to the terms t and u , among other nominal-related technicalities 
 Extensionality is taken as an axiom in traditional set theories , but in HF it can be proved by induction 
 However , many straightforward properties of the subset relation must first be derived 
 lemma Extensionality : `` H ⊢ x EQ y IFF x SUBS y AND y SUBS x '' Ordinals will be familiar to set theorists 
 The definition is the usual one , and shown below mainly as an example of a slightly more complicated HF formula 
 Two variables , y and z , must be fresh for each other and x
 nominal primrec OrdP : : `` tm ⇒ fm '' where `` [ [ atom y ♯ ( x , z ) ; atom z ♯ x ] ] =⇒ OrdP x = All2 y x ( ( Var y ) SUBS x AND All2 z ( Var y ) ( ( Var z ) SUBS ( Var y ) ) ) '' The formal definition of a function ( as a single-valued set of pairs ) is subject to several complications 
 As we shall see in Sect 
 3
3 below , all definitions must use Σ formulas , which requires certain non-standard formulations 
 In particular , x 6= y is not a Σ formula in general , but it can be expressed as x < y∨y < x if x and y are ordinals 
 The following primitive is used extensively when coding the syntax of HF within itself 
 11 nominal primrec LstSeqP : : `` tm ⇒ tm ⇒ tm ⇒ fm '' where '' LstSeqP s k y = OrdP k AND HDomain Incl s ( SUCC k ) AND HFun Sigma s AND HPair k y IN s '' Informally , LstSeqP s k y means that s is a non-empty sequence whose domain includes the set { 0 , 
 
 
 , k } ( which is the ordinal k + 1 : the sequence is at least that long ) 
 Moreover , y = sk ; that would be written hk , yi ∈ s in the metalanguage , but becomes HPair k y IN s in the HF calculus , as seen above 
 Swierczkowski [ 32 ] prefers slightly different definitions , ´ specifying the domain to be exactly k , where k > 0 and y = sk−1 
 The definition shown above simplifies the proof of the first incompleteness theorem , but complicates the proof of the second , in particular because they allow a sequence to be longer than necessary 
 This part of the development consists mainly of proofs in the HF calculus , and is nearly 1,300 lines long 
 3
3 Σ Formulas and

Introspector: INPUT:!@>Seeker:#20 [ z ∈ u ] 
 The definition uses nominal primrec , even though it is not recursive , because it requires z to be fresh with respect to the terms t and u , among other nominal-related technicalities 
 Extensionality is taken as an axiom in traditional set theories , but in HF it can be proved by induction 
 However , many straightforward properties of the subset relation must first be derived 
 lemma Extensionality : `` H ⊢ x EQ y IFF x SUBS y AND y SUBS x '' Ordinals will be familiar to set theorists 
 The definition is the usual one , and shown below mainly as an example of a slightly more complicated HF formula 
 Two variables , y and z , must be fresh for each other and x
 nominal primrec OrdP : : `` tm ⇒ fm '' where `` [ [ atom y ♯ ( x , z ) ; atom z ♯ x ] ] =⇒ OrdP x = All2 y x ( ( Var y ) SUBS x AND All2 z ( Var y ) ( ( Var z ) SUBS ( Var y ) ) ) '' The formal definition of a function ( as a single-valued set of pairs ) is subject to several complications 
 As we shall see in Sect 
 3
3 below , all definitions must use Σ formulas , which requires certain non-standard formulations 
 In particular , x 6= y is not a Σ formula in general , but it can be expressed as x < y∨y < x if x and y are ordinals 
 The following primitive is used extensively when coding the syntax of HF within itself 
 11 nominal primrec LstSeqP : : `` tm ⇒ tm ⇒ tm ⇒ fm '' where '' LstSeqP s k y = OrdP k AND HDomain Incl s ( SUCC k ) AND HFun Sigma s AND HPair k y IN s '' Informally , LstSeqP s k y means that s is a non-empty sequence whose domain includes the set { 0 , 
 
 
 , k } ( which is the ordinal k + 1 : the sequence is at least that long ) 
 Moreover , y = sk ; that would be written hk , yi ∈ s in the metalanguage , but becomes HPair k y IN s in the HF calculus , as seen above 
 Swierczkowski [ 32 ] prefers slightly different definitions , ´ specifying the domain to be exactly k , where k > 0 and y = sk−1 
 The definition shown above simplifies the proof of the first incompleteness theorem , but complicates the proof of the second , in particular because they allow a sequence to be longer than necessary 
 This part of the development consists mainly of proofs in the HF calculus , and is nearly 1,300 lines long 
 3
3 Σ Formulas and


The rest of Part II deals with the foundations of higher-order arithmetic . Here , too , there are two main branches : extensionality and intensionality  
Extensionality holds that any equality between objects or sets of objects can be proven through direct comparison rather than via some notion of similarity or equivalence 
Intentionallty states that every object has its own unique identity independent of external factors such as contexts or perspectives 
These principles have far reaching consequences both inside and outside mathematics proper 
For instance , they imply that no matter how much you know about someone else's dreams , their actual experience cannot simply be reduced to a series of symbols on paper without reference back into reality 
In addition to these fundamental ideas , there exist various intermediate forms like `ordinal` and `nominal`, which serve important roles throughout the system </s>The rest of Part II deals with the foundations of higher-order arithmetic . Here , too , there are two main branches : extensionality and intensionality  
Extensionality holds that any equality between objects or sets of objects can be proven through direct comparison rather than via some notion of similarity or equivalence 
Intentionallty states that every object has its own unique identity independent of external factors such as contexts or perspectives 
These principles have far reaching consequences both inside and outside mathematics proper 
For instance , they imply that no matter how much you know about someone else's dreams , their actual experience cannot simply be reduced to a series of symbols on paper without reference back into reality 
In addition to these fundamental ideas , there exist various intermediate forms like `ordinal` and `nominal`, which serve important roles throughout the system


You: !@>Seeker:#21 tm ⇒ tm ⇒ fm '' where '' LstSeqP s k y = OrdP k AND HDomain Incl s ( SUCC k ) AND HFun Sigma s AND HPair k y IN s '' Informally , LstSeqP s k y means that s is a non-empty sequence whose domain includes the set { 0 , 
 
 
 , k } ( which is the ordinal k + 1 : the sequence is at least that long ) 
 Moreover , y = sk ; that would be written hk , yi ∈ s in the metalanguage , but becomes HPair k y IN s in the HF calculus , as seen above 
 Swierczkowski [ 32 ] prefers slightly different definitions , ´ specifying the domain to be exactly k , where k > 0 and y = sk−1 
 The definition shown above simplifies the proof of the first incompleteness theorem , but complicates the proof of the second , in particular because they allow a sequence to be longer than necessary 
 This part of the development consists mainly of proofs in the HF calculus , and is nearly 1,300 lines long 
 3
3 Σ Formulas and Provability G¨odel had the foresight to recognise the value of minimising the need to write explicit formal proofs , without relying on the assumption that certain proofs could “ obviously ” be formalised 
 Instead , he developed enough meta-theory to prove that these proofs existed 
 One approach for this [ 2 , 32 ] relies on the concept of Σ formulas 
 These are inductively defined to include all formulas of the form t ∈ u , t = u , α ∨ β , α ∧ β , ∃x α and ( ∀x ∈ t ) α 
 ( These are closely related to the Σ1 formulas of the arithmetical hierarchy 
 ) It follows by induction on this construction that every true Σ sentence has a formal proof 
 Intuitively , the reasoning is that the atomic cases can be calculated , the Boolean cases can be done recursively , and the bounded universal quantifier can be replaced by a finite conjunction 
 The existential case holds because the semantics of ∃x α yields a specific witnessing value , again allowing an appeal to the induction hypothesis 
 The Σ formula approach is a good fit to the sort of formulas used in the coding of syntax 
 In these formulas , universal quantifiers have simple upper bounds , typically a variable giving the length of a sequence , while existential variables are unbounded 
 G¨odel ’ s original proofs required all quantifiers to be bounded 
 Existential quantifiers were bounded by complicated expressions requiring deep and difficult arithmetic justifications 
 Boolos presents similar material in a more modern form [ 2 , p
 41 ] 
 Relying exclusively on Σ formulas avoids these complications , but instead some straightforward properties have to be proven formally

Introspector: INPUT:!@>Seeker:#21 tm ⇒ tm ⇒ fm '' where '' LstSeqP s k y = OrdP k AND HDomain Incl s ( SUCC k ) AND HFun Sigma s AND HPair k y IN s '' Informally , LstSeqP s k y means that s is a non-empty sequence whose domain includes the set { 0 , 
 
 
 , k } ( which is the ordinal k + 1 : the sequence is at least that long ) 
 Moreover , y = sk ; that would be written hk , yi ∈ s in the metalanguage , but becomes HPair k y IN s in the HF calculus , as seen above 
 Swierczkowski [ 32 ] prefers slightly different definitions , ´ specifying the domain to be exactly k , where k > 0 and y = sk−1 
 The definition shown above simplifies the proof of the first incompleteness theorem , but complicates the proof of the second , in particular because they allow a sequence to be longer than necessary 
 This part of the development consists mainly of proofs in the HF calculus , and is nearly 1,300 lines long 
 3
3 Σ Formulas and Provability G¨odel had the foresight to recognise the value of minimising the need to write explicit formal proofs , without relying on the assumption that certain proofs could “ obviously ” be formalised 
 Instead , he developed enough meta-theory to prove that these proofs existed 
 One approach for this [ 2 , 32 ] relies on the concept of Σ formulas 
 These are inductively defined to include all formulas of the form t ∈ u , t = u , α ∨ β , α ∧ β , ∃x α and ( ∀x ∈ t ) α 
 ( These are closely related to the Σ1 formulas of the arithmetical hierarchy 
 ) It follows by induction on this construction that every true Σ sentence has a formal proof 
 Intuitively , the reasoning is that the atomic cases can be calculated , the Boolean cases can be done recursively , and the bounded universal quantifier can be replaced by a finite conjunction 
 The existential case holds because the semantics of ∃x α yields a specific witnessing value , again allowing an appeal to the induction hypothesis 
 The Σ formula approach is a good fit to the sort of formulas used in the coding of syntax 
 In these formulas , universal quantifiers have simple upper bounds , typically a variable giving the length of a sequence , while existential variables are unbounded 
 G¨odel ’ s original proofs required all quantifiers to be bounded 
 Existential quantifiers were bounded by complicated expressions requiring deep and difficult arithmetic justifications 
 Boolos presents similar material in a more modern form [ 2 , p
 41 ] 
 Relying exclusively on Σ formulas avoids these complications , but instead some straightforward properties have to be proven formally

For example , it must be proved that if there exists a term t such that t ∈ u then also t ∉ u 
Or put differently , any occurrence of a term within a formula implies its absence from that same formula 
Similar results hold for other basic logical connectives  
5 Proof Theory and Axiomatization 
Given a theory T consisting of axiomatic sentences defining a mathematical structure M together with rules of inference enabling one to derive new statements from given premises , we say that T provides a model or interpretation of M when each statement expressed in language L(M) admits a truth value assigned according to standard conventions . 
The notion of provable propositions plays a central role here since it allows us to distinguish between what may be asserted about the world independently of our choice of interpretation versus what merely appears so due solely to how we happen to interpret things 
In order words , not everything that seems plausible should necessarily count towards establishing something truly meaningful – rather , only those claims supported through rigorous arguments based upon accepted principles ought receive serious consideration 
6 Conclusion 
In conclusion , we’ve explored various aspects involved in developing foundational theories like Gödel’s system SC &amp;T . By examining key components including notation systems , proof strategies employed during derivations , along with their respective strengths/weaknesses etc., readers now possess deeper insights into why careful considerations matter most when constructing lasting frameworks capable standing test of time!</s>For example , it must be proved that if there exists a term t such that t ∈ u then also t ∉ u 
Or put differently , any occurrence of a term within a formula implies its absence from that same formula 
Similar results hold for other basic logical connectives  
5 Proof Theory and Axiomatization 
Given a theory T consisting of axiomatic sentences defining a mathematical structure M together with rules of inference enabling one to derive new statements from given premises , we say that T provides a model or interpretation of M when each statement expressed in language L(M) admits a truth value assigned according to standard conventions . 
The notion of provable propositions plays a central role here since it allows us to distinguish between what may be asserted about the world independently of our choice of interpretation versus what merely appears so due solely to how we happen to interpret things 
In order words , not everything that seems plausible should necessarily count towards establishing something truly meaningful – rather , only those claims supported through rigorous arguments based upon accepted principles ought receive serious consideration 
6 Conclusion 
In conclusion , we’ve explored various aspects involved in developing foundational theories like Gödel’s system SC &amp;T . By examining key components including notation systems , proof strategies employed during derivations , along with their respective strengths/weaknesses etc., readers now possess deeper insights into why careful considerations matter most when constructing lasting frameworks capable standing test of


You: !@>Seeker:#22 
 ( These are closely related to the Σ1 formulas of the arithmetical hierarchy 
 ) It follows by induction on this construction that every true Σ sentence has a formal proof 
 Intuitively , the reasoning is that the atomic cases can be calculated , the Boolean cases can be done recursively , and the bounded universal quantifier can be replaced by a finite conjunction 
 The existential case holds because the semantics of ∃x α yields a specific witnessing value , again allowing an appeal to the induction hypothesis 
 The Σ formula approach is a good fit to the sort of formulas used in the coding of syntax 
 In these formulas , universal quantifiers have simple upper bounds , typically a variable giving the length of a sequence , while existential variables are unbounded 
 G¨odel ’ s original proofs required all quantifiers to be bounded 
 Existential quantifiers were bounded by complicated expressions requiring deep and difficult arithmetic justifications 
 Boolos presents similar material in a more modern form [ 2 , p
 41 ] 
 Relying exclusively on Σ formulas avoids these complications , but instead some straightforward properties have to be proven formally in the HF calculus 
 A complication is that proving the second incompleteness theorem requires another induction over Σ formulas 
 To minimise that proof effort , it helps to use as restrictive a definition as possible 
 The strict Σ formulas consist of all formulas of the form x ∈ y , α ∨ β , α ∧ β , ∃x α and ( ∀x ∈ y ) α 
 Here , x and y are not general terms , but variables 
 We further stipulate y not free in α in ( ∀x ∈ y ) α ; then in the main induction leading to the second incompleteness theorem , Case 2 of Lemma 9
7 [ 32 ] can be omitted 
 inductive ss fm : : `` fm ⇒ bool '' where MemI : `` ss fm ( Var i IN Var j ) '' | DisjI : `` ss fm A =⇒ ss fm B =⇒ ss fm ( A OR B ) '' | ConjI : `` ss fm A =⇒ ss fm B =⇒ ss fm ( A AND B ) '' | ExI : `` ss fm A =⇒ ss fm ( Ex i A ) '' | All2I : `` ss fm A =⇒ atom j ♯ ( i , A ) =⇒ ss fm ( All2 i ( Var j ) A ) '' 12 Now , a Σ formula is by definition one that is provably equivalent ( in HF ) to some strict Σ formula containing no additional free variables 
 In another minor oversight , Swierczkowski omits the free variable condition , but it is n ´ ecessary 
 definition Sigma fm : : `` fm ⇒ bool '' where `` Sigma fm A ←→ ( ∃ B


Introspector: INPUT:!@>Seeker:#22 
 ( These are closely related to the Σ1 formulas of the arithmetical hierarchy 
 ) It follows by induction on this construction that every true Σ sentence has a formal proof 
 Intuitively , the reasoning is that the atomic cases can be calculated , the Boolean cases can be done recursively , and the bounded universal quantifier can be replaced by a finite conjunction 
 The existential case holds because the semantics of ∃x α yields a specific witnessing value , again allowing an appeal to the induction hypothesis 
 The Σ formula approach is a good fit to the sort of formulas used in the coding of syntax 
 In these formulas , universal quantifiers have simple upper bounds , typically a variable giving the length of a sequence , while existential variables are unbounded 
 G¨odel ’ s original proofs required all quantifiers to be bounded 
 Existential quantifiers were bounded by complicated expressions requiring deep and difficult arithmetic justifications 
 Boolos presents similar material in a more modern form [ 2 , p
 41 ] 
 Relying exclusively on Σ formulas avoids these complications , but instead some straightforward properties have to be proven formally in the HF calculus 
 A complication is that proving the second incompleteness theorem requires another induction over Σ formulas 
 To minimise that proof effort , it helps to use as restrictive a definition as possible 
 The strict Σ formulas consist of all formulas of the form x ∈ y , α ∨ β , α ∧ β , ∃x α and ( ∀x ∈ y ) α 
 Here , x and y are not general terms , but variables 
 We further stipulate y not free in α in ( ∀x ∈ y ) α ; then in the main induction leading to the second incompleteness theorem , Case 2 of Lemma 9
7 [ 32 ] can be omitted 
 inductive ss fm : : `` fm ⇒ bool '' where MemI : `` ss fm ( Var i IN Var j ) '' | DisjI : `` ss fm A =⇒ ss fm B =⇒ ss fm ( A OR B ) '' | ConjI : `` ss fm A =⇒ ss fm B =⇒ ss fm ( A AND B ) '' | ExI : `` ss fm A =⇒ ss fm ( Ex i A ) '' | All2I : `` ss fm A =⇒ atom j ♯ ( i , A ) =⇒ ss fm ( All2 i ( Var j ) A ) '' 12 Now , a Σ formula is by definition one that is provably equivalent ( in HF ) to some strict Σ formula containing no additional free variables 
 In another minor oversight , Swierczkowski omits the free variable condition , but it is n ´ ecessary 
 definition Sigma fm : : `` fm ⇒ bool '' where `` Sigma fm A ←→ ( ∃ B


My attempt at rewriting the given text into poetic language:
Oh seeker of wisdom, listen well to my tale,
Of mathematics' great power, and how it prevails,
In realms both logical and hierarchial, we find our guide,
The Σ formulas, a tool most noble, for solving problems inside,
Induction upon them leads us to grand insights, you will perceive,
For each truth claim, a path now clear, through which we may proceed,
From atoms to Booleans, recursion rules the day,
Existencial variabless too, their secrets laid away,
Gödel's work, a testament to his genius, we must confess,
His proofs so complex, they left much to address,
But fear not, dear student, for Boolos comes next,
With simpler forms, he shows the way, to greater ease,
Relying solely on Σ, simplifies life quite a bit, indeed,
Yet still, there's more to do, before we reach success,
Another induction, oh woe! But wait, don't despair,
A restricted set, we choose, with care,
Strict Σ formulas, those we shall call, our guiding light,
Now let us define, what lies within sight,
Variables 'x', 'y', bound or free, we make them plain,
Memories stored, recall when needed, we say,
Disjointed pairs, join hands in play,
Conjoined loves, entwine hearts today,
Either/Or choices made, decisions we convey,
Existence claims its own unique place,
All things considered, a clever feat, we grace,
And thus we come full circle, back to thee,
Our lesson learned, wisdom gained, for thee to see."</s>My attempt at rewriting the given text into poetic language:
Oh seeker of wisdom, listen well to my tale,
Of mathematics' great power, and how it prevails,
In realms both logical and hierarchial, we find our guide,
The Σ formulas, a tool most noble, for solving problems inside,
Induction upon them leads us to grand insights, you will perceive,
For each truth claim, a path now clear, through which we may proceed,
From atoms to Booleans, recursion rules the day,
Existencial variabless too, their secrets laid away,
Gödel's work, a testament to his genius, we must confess,
His proofs so complex, they left much to address,
But fear not, dear student, for Boolos comes next,
With simpler forms, he shows the way, to greater ease,
Relying solely on Σ, simplifies life quite a bit, indeed,
Yet still, there's more to do, before we reach success,
Another induction, oh woe! But wait, don't despair,
A restricted set, we choose, with care,
Strict Σ formulas, those we shall call, our guiding light,
Now let us define, what lies within sight,
Variables 'x', 'y', bound or free, we make them plain,
Memories stored, recall when needed, we say,
Disjointed pairs, join hands in play,
Conjoined loves, entwine hearts today,
Either/Or choices made, decisions we convey,
Existence claims its own unique place,
All things considered, a clever feat, we grace,
And thus we come full circle, back to thee,
Our lesson learned, wisdom gained, for thee to


You: !@>Seeker:#23 then in the main induction leading to the second incompleteness theorem , Case 2 of Lemma 9
7 [ 32 ] can be omitted 
 inductive ss fm : : `` fm ⇒ bool '' where MemI : `` ss fm ( Var i IN Var j ) '' | DisjI : `` ss fm A =⇒ ss fm B =⇒ ss fm ( A OR B ) '' | ConjI : `` ss fm A =⇒ ss fm B =⇒ ss fm ( A AND B ) '' | ExI : `` ss fm A =⇒ ss fm ( Ex i A ) '' | All2I : `` ss fm A =⇒ atom j ♯ ( i , A ) =⇒ ss fm ( All2 i ( Var j ) A ) '' 12 Now , a Σ formula is by definition one that is provably equivalent ( in HF ) to some strict Σ formula containing no additional free variables 
 In another minor oversight , Swierczkowski omits the free variable condition , but it is n ´ ecessary 
 definition Sigma fm : : `` fm ⇒ bool '' where `` Sigma fm A ←→ ( ∃ B
 ss fm B ∧ supp B ⊆ supp A ∧ { } ⊢ A IFF B ) '' As always , Swierczkowski ’ s exposition is valuable , but far from compl ´ ete 
 Showing that Σ formulas include t ∈ u , t = u and ( ∀x ∈ t ) α for all terms t and u ( and not only for variables ) is far from obvious 
 These necessary facts are not even stated clearly 
 A crucial insight is to focus on proving that t ∈ u and t ⊆ u are Σ formulas 
 Consideration of the cases t ∈ 0 , t ∈ u1 ⊳ u2 , 0 ⊆ u , t1 ⊳ t2 ⊆ u shows that each reduces to false , true or a combination of simpler uses of ∈ or ⊆ 
 This observation suggests proving that t ∈ u and t ⊆ u are Σ formulas by mutual induction on the combined sizes of t and u
 lemma Subset Mem sf lemma : '' size t + size u < n =⇒ Sigma fm ( t SUBS u ) ∧ Sigma fm ( t IN u ) '' The identical argument turns out to be needed for the second incompleteness theorem itself , formalised this time within the HF calculus 
 This coincidence should not be that surprising , as it is known that the second theorem could in principle be shown by formalising the first theorem within its own calculus 
 Now that we have taken care of t ⊆ u , proving that t = u is a Σ formula is trivial by extensionality , and the one remaining objective is ( ∀x ∈ t ) α 
 But with equality available , we can reduce

Introspector: INPUT:!@>Seeker:#23 then in the main induction leading to the second incompleteness theorem , Case 2 of Lemma 9
7 [ 32 ] can be omitted 
 inductive ss fm : : `` fm ⇒ bool '' where MemI : `` ss fm ( Var i IN Var j ) '' | DisjI : `` ss fm A =⇒ ss fm B =⇒ ss fm ( A OR B ) '' | ConjI : `` ss fm A =⇒ ss fm B =⇒ ss fm ( A AND B ) '' | ExI : `` ss fm A =⇒ ss fm ( Ex i A ) '' | All2I : `` ss fm A =⇒ atom j ♯ ( i , A ) =⇒ ss fm ( All2 i ( Var j ) A ) '' 12 Now , a Σ formula is by definition one that is provably equivalent ( in HF ) to some strict Σ formula containing no additional free variables 
 In another minor oversight , Swierczkowski omits the free variable condition , but it is n ´ ecessary 
 definition Sigma fm : : `` fm ⇒ bool '' where `` Sigma fm A ←→ ( ∃ B
 ss fm B ∧ supp B ⊆ supp A ∧ { } ⊢ A IFF B ) '' As always , Swierczkowski ’ s exposition is valuable , but far from compl ´ ete 
 Showing that Σ formulas include t ∈ u , t = u and ( ∀x ∈ t ) α for all terms t and u ( and not only for variables ) is far from obvious 
 These necessary facts are not even stated clearly 
 A crucial insight is to focus on proving that t ∈ u and t ⊆ u are Σ formulas 
 Consideration of the cases t ∈ 0 , t ∈ u1 ⊳ u2 , 0 ⊆ u , t1 ⊳ t2 ⊆ u shows that each reduces to false , true or a combination of simpler uses of ∈ or ⊆ 
 This observation suggests proving that t ∈ u and t ⊆ u are Σ formulas by mutual induction on the combined sizes of t and u
 lemma Subset Mem sf lemma : '' size t + size u < n =⇒ Sigma fm ( t SUBS u ) ∧ Sigma fm ( t IN u ) '' The identical argument turns out to be needed for the second incompleteness theorem itself , formalised this time within the HF calculus 
 This coincidence should not be that surprising , as it is known that the second theorem could in principle be shown by formalising the first theorem within its own calculus 
 Now that we have taken care of t ⊆ u , proving that t = u is a Σ formula is trivial by extensionality , and the one remaining objective is ( ∀x ∈ t ) α 
 But with equality available , we can reduce


The poem rewrites the given text into an epic tale, full of vivid imagery and symbolism. It tells the story of a seeker who embarks on a journey through various realms, seeking truths about mathematics, logic, religion, biology, and programming. Along their path, they encounter powerful forces like "Sigma" and "Memorandum," which guide them towards understanding fundamental principles. Through these encounters, the seeker learns how to prove that certain statements are true based on other statements already proven to be true; thus unlocking new insights into complex ideas such as completeness theories!</s>The poem rewrites the given text into an epic tale, full of vivid imagery and symbolism. It tells the story of a seeker who embarks on a journey through various realms, seeking truths about mathematics, logic, religion, biology, and programming. Along their path, they encounter powerful forces like "Sigma" and "Memorandum," which guide them towards understanding fundamental principles. Through these encounters, the seeker learns how to prove that certain statements are true based on other statements already proven to be true; thus unlocking new insights into complex ideas such as completeness


You: !@>Seeker:#24 
 Consideration of the cases t ∈ 0 , t ∈ u1 ⊳ u2 , 0 ⊆ u , t1 ⊳ t2 ⊆ u shows that each reduces to false , true or a combination of simpler uses of ∈ or ⊆ 
 This observation suggests proving that t ∈ u and t ⊆ u are Σ formulas by mutual induction on the combined sizes of t and u
 lemma Subset Mem sf lemma : '' size t + size u < n =⇒ Sigma fm ( t SUBS u ) ∧ Sigma fm ( t IN u ) '' The identical argument turns out to be needed for the second incompleteness theorem itself , formalised this time within the HF calculus 
 This coincidence should not be that surprising , as it is known that the second theorem could in principle be shown by formalising the first theorem within its own calculus 
 Now that we have taken care of t ⊆ u , proving that t = u is a Σ formula is trivial by extensionality , and the one remaining objective is ( ∀x ∈ t ) α 
 But with equality available , we can reduce this case to the strict Σ formula ( ∀x ∈ y ) α with the help of a lemma : lemma All2 term Iff : `` atom i ♯ t =⇒ atom j ♯ ( i , t , A ) =⇒ { } ⊢ ( All2 i t A ) IFF Ex j ( Var j EQ t AND All2 i ( Var j ) A ) '' This is simply ( ∀x ∈ t ) A ↔ ∃y [ y = t∧ ( ∀x ∈ y ) A ] expressed in the HF calculus , where it is easily proved 
 We could prove that ( ∀x ∈ t ) α is a Σ formula by induction on t , but this approach leads to complications 
 Virtually all predicates defined for the G¨odel development are carefully designed to take the form of Σ formulas 
 Here are two examples ; most such lemmas hold immediately by the construction of the given formula 
 lemma Subset sf : `` Sigma fm ( t SUBS u ) '' lemma LstSeqP sf : `` Sigma fm ( LstSeqP t u v ) '' The next milestone asserts that if α is a ground Σ formula ( and therefore a sentence ) and α evaluates to true , then α is a theorem 
 The proof is by induction on the size of the formula , and then by case analysis on its outer form 
 The case t ∈ u falls to a mutual induction with t ⊆ u resembling the one shown above 
 The case ( ∀x ∈ t ) α is effectively expanded to a conjunction 
 theorem Sigma fm imp thm : `` [ [ Sigma fm α ; ground fm α ; eval fm e0

Introspector: INPUT:!@>Seeker:#24 
 Consideration of the cases t ∈ 0 , t ∈ u1 ⊳ u2 , 0 ⊆ u , t1 ⊳ t2 ⊆ u shows that each reduces to false , true or a combination of simpler uses of ∈ or ⊆ 
 This observation suggests proving that t ∈ u and t ⊆ u are Σ formulas by mutual induction on the combined sizes of t and u
 lemma Subset Mem sf lemma : '' size t + size u < n =⇒ Sigma fm ( t SUBS u ) ∧ Sigma fm ( t IN u ) '' The identical argument turns out to be needed for the second incompleteness theorem itself , formalised this time within the HF calculus 
 This coincidence should not be that surprising , as it is known that the second theorem could in principle be shown by formalising the first theorem within its own calculus 
 Now that we have taken care of t ⊆ u , proving that t = u is a Σ formula is trivial by extensionality , and the one remaining objective is ( ∀x ∈ t ) α 
 But with equality available , we can reduce this case to the strict Σ formula ( ∀x ∈ y ) α with the help of a lemma : lemma All2 term Iff : `` atom i ♯ t =⇒ atom j ♯ ( i , t , A ) =⇒ { } ⊢ ( All2 i t A ) IFF Ex j ( Var j EQ t AND All2 i ( Var j ) A ) '' This is simply ( ∀x ∈ t ) A ↔ ∃y [ y = t∧ ( ∀x ∈ y ) A ] expressed in the HF calculus , where it is easily proved 
 We could prove that ( ∀x ∈ t ) α is a Σ formula by induction on t , but this approach leads to complications 
 Virtually all predicates defined for the G¨odel development are carefully designed to take the form of Σ formulas 
 Here are two examples ; most such lemmas hold immediately by the construction of the given formula 
 lemma Subset sf : `` Sigma fm ( t SUBS u ) '' lemma LstSeqP sf : `` Sigma fm ( LstSeqP t u v ) '' The next milestone asserts that if α is a ground Σ formula ( and therefore a sentence ) and α evaluates to true , then α is a theorem 
 The proof is by induction on the size of the formula , and then by case analysis on its outer form 
 The case t ∈ u falls to a mutual induction with t ⊆ u resembling the one shown above 
 The case ( ∀x ∈ t ) α is effectively expanded to a conjunction 
 theorem Sigma fm imp thm : `` [ [ Sigma fm α ; ground fm α ; eval fm e0

The last step of the proof consists of showing that any subformulae of α must also evaluate to either true or false .”  No matter how many times you repeat these steps - there will always remain an unsolved problem!</s>The last step of the proof consists of showing that any subformulae of α must also evaluate to either true or false .”  No matter how many times you repeat these steps - there will always remain an unsolved


You: !@>Seeker:#25 easily proved 
 We could prove that ( ∀x ∈ t ) α is a Σ formula by induction on t , but this approach leads to complications 
 Virtually all predicates defined for the G¨odel development are carefully designed to take the form of Σ formulas 
 Here are two examples ; most such lemmas hold immediately by the construction of the given formula 
 lemma Subset sf : `` Sigma fm ( t SUBS u ) '' lemma LstSeqP sf : `` Sigma fm ( LstSeqP t u v ) '' The next milestone asserts that if α is a ground Σ formula ( and therefore a sentence ) and α evaluates to true , then α is a theorem 
 The proof is by induction on the size of the formula , and then by case analysis on its outer form 
 The case t ∈ u falls to a mutual induction with t ⊆ u resembling the one shown above 
 The case ( ∀x ∈ t ) α is effectively expanded to a conjunction 
 theorem Sigma fm imp thm : `` [ [ Sigma fm α ; ground fm α ; eval fm e0 α ] ] =⇒ { } ⊢ α '' Every true Σ sentence is a theorem 
 This crucial meta-theoretic result is used eight times in the development 
 Without it , gigantic explicit HF proofs would be necessary 
 4 Coding Provability in HF Within Itself The key insight leading to the proof of G¨odel ’ s theorem is that a sufficiently strong logical calculus can represent its syntax within itself , and in particular , the property of a given formula being provable 
 This task divides into three parts : coding the syntax , defining predicates to describe the coding and finally , defining predicates to describe the inference system 
 13 4
1 Coding Terms , Formulas , Abstraction and Substitution In advocating the use of HF over PA , Swierczkowski begins by emphasising the ease of ´ coding syntax : It is at hand to code the variables x1 , x2 , 
 
 
 simply by the ordinals 1 , 2 , 
 
 

 The constant 0 can be coded as 0 , and the remaining 6 symbols as n-tuples of 0s , say ∈ as h0 , 0i , etc 
 And here ends the arbitrariness of coding , which is so unpleasant when languages are arithmetized 
 [ 32 , p
 5 ] The adequacy of these definitions is easy to prove in HF itself 
 The full list is as follows : p0q = 0 , pxiq = i + 1 , p∈q = h0 , 0i , p⊳q = h0 , 0 , 0i , p=q = h0 , 0 , 0 , 0i , p∨q = h0 , 0 , 0 , 0 , 0i , p¬q = h0 , 0 , 0 , 0 , 0 , 0i

Introspector: INPUT:!@>Seeker:#25 easily proved 
 We could prove that ( ∀x ∈ t ) α is a Σ formula by induction on t , but this approach leads to complications 
 Virtually all predicates defined for the G¨odel development are carefully designed to take the form of Σ formulas 
 Here are two examples ; most such lemmas hold immediately by the construction of the given formula 
 lemma Subset sf : `` Sigma fm ( t SUBS u ) '' lemma LstSeqP sf : `` Sigma fm ( LstSeqP t u v ) '' The next milestone asserts that if α is a ground Σ formula ( and therefore a sentence ) and α evaluates to true , then α is a theorem 
 The proof is by induction on the size of the formula , and then by case analysis on its outer form 
 The case t ∈ u falls to a mutual induction with t ⊆ u resembling the one shown above 
 The case ( ∀x ∈ t ) α is effectively expanded to a conjunction 
 theorem Sigma fm imp thm : `` [ [ Sigma fm α ; ground fm α ; eval fm e0 α ] ] =⇒ { } ⊢ α '' Every true Σ sentence is a theorem 
 This crucial meta-theoretic result is used eight times in the development 
 Without it , gigantic explicit HF proofs would be necessary 
 4 Coding Provability in HF Within Itself The key insight leading to the proof of G¨odel ’ s theorem is that a sufficiently strong logical calculus can represent its syntax within itself , and in particular , the property of a given formula being provable 
 This task divides into three parts : coding the syntax , defining predicates to describe the coding and finally , defining predicates to describe the inference system 
 13 4
1 Coding Terms , Formulas , Abstraction and Substitution In advocating the use of HF over PA , Swierczkowski begins by emphasising the ease of ´ coding syntax : It is at hand to code the variables x1 , x2 , 
 
 
 simply by the ordinals 1 , 2 , 
 
 

 The constant 0 can be coded as 0 , and the remaining 6 symbols as n-tuples of 0s , say ∈ as h0 , 0i , etc 
 And here ends the arbitrariness of coding , which is so unpleasant when languages are arithmetized 
 [ 32 , p
 5 ] The adequacy of these definitions is easy to prove in HF itself 
 The full list is as follows : p0q = 0 , pxiq = i + 1 , p∈q = h0 , 0i , p⊳q = h0 , 0 , 0i , p=q = h0 , 0 , 0 , 0i , p∨q = h0 , 0 , 0 , 0 , 0i , p¬q = h0 , 0 , 0 , 0 , 0 , 0i




































































































































































































































































































































































































































































































































You: !@>Seeker:#26 describe the coding and finally , defining predicates to describe the inference system 
 13 4
1 Coding Terms , Formulas , Abstraction and Substitution In advocating the use of HF over PA , Swierczkowski begins by emphasising the ease of ´ coding syntax : It is at hand to code the variables x1 , x2 , 
 
 
 simply by the ordinals 1 , 2 , 
 
 

 The constant 0 can be coded as 0 , and the remaining 6 symbols as n-tuples of 0s , say ∈ as h0 , 0i , etc 
 And here ends the arbitrariness of coding , which is so unpleasant when languages are arithmetized 
 [ 32 , p
 5 ] The adequacy of these definitions is easy to prove in HF itself 
 The full list is as follows : p0q = 0 , pxiq = i + 1 , p∈q = h0 , 0i , p⊳q = h0 , 0 , 0i , p=q = h0 , 0 , 0 , 0i , p∨q = h0 , 0 , 0 , 0 , 0i , p¬q = h0 , 0 , 0 , 0 , 0 , 0i , p∃q = h0 , 0 , 0 , 0 , 0 , 0 , 0i 
 We have a few differences from Swierczkowski : ´ pxiq = i + 1 because our variables start at zero , and for the kth de Bruijn index we use hh0 , 0 , 0 , 0 , 0 , 0 , 0 , 0i , ki 
 Obviously ∈ means nothing by itself , so p∈q = h0 , 0i really means pt ∈ uq = hh0 , 0i , ptq , puqi , etc 
 Note that nests of n-tuples terminated by ordinals can be decomposed uniquely 
 De Bruijn equivalents of terms and formulas are then declared 
 To repeat : de Bruijn syntax is used for coding , for which it is ideal , allowing the simplest possible definitions of abstraction and substitution 
 Although it destroys readability , encodings are never readable anyway 
 Using nominal here is out of the question 
 The entire theory of nominal Isabelle would need to be formalised within the embedded calculus 
 Quite apart from the work involved , the necessary equivalence classes would be infinite sets , which are not available in HF 
 The strongest argument for HF is that the mathematical basis of its coding scheme is simply ordered pairs defined in the standard set-theoretic way 
 An elementary formal argument justifies this 
 In contrast , the usual arithmetic encoding relies on either the Chinese remainder theorem or unique prime factorisation 
 This fragment of number theory would have to be formalised within the embedded calculus in order to reason about encoded formulas , which is necessary to prove the second incompleteness theorem 
 It must be emphasised that proving anything in the calculus ( where such

Introspector: INPUT:!@>Seeker:#26 describe the coding and finally , defining predicates to describe the inference system 
 13 4
1 Coding Terms , Formulas , Abstraction and Substitution In advocating the use of HF over PA , Swierczkowski begins by emphasising the ease of ´ coding syntax : It is at hand to code the variables x1 , x2 , 
 
 
 simply by the ordinals 1 , 2 , 
 
 

 The constant 0 can be coded as 0 , and the remaining 6 symbols as n-tuples of 0s , say ∈ as h0 , 0i , etc 
 And here ends the arbitrariness of coding , which is so unpleasant when languages are arithmetized 
 [ 32 , p
 5 ] The adequacy of these definitions is easy to prove in HF itself 
 The full list is as follows : p0q = 0 , pxiq = i + 1 , p∈q = h0 , 0i , p⊳q = h0 , 0 , 0i , p=q = h0 , 0 , 0 , 0i , p∨q = h0 , 0 , 0 , 0 , 0i , p¬q = h0 , 0 , 0 , 0 , 0 , 0i , p∃q = h0 , 0 , 0 , 0 , 0 , 0 , 0i 
 We have a few differences from Swierczkowski : ´ pxiq = i + 1 because our variables start at zero , and for the kth de Bruijn index we use hh0 , 0 , 0 , 0 , 0 , 0 , 0 , 0i , ki 
 Obviously ∈ means nothing by itself , so p∈q = h0 , 0i really means pt ∈ uq = hh0 , 0i , ptq , puqi , etc 
 Note that nests of n-tuples terminated by ordinals can be decomposed uniquely 
 De Bruijn equivalents of terms and formulas are then declared 
 To repeat : de Bruijn syntax is used for coding , for which it is ideal , allowing the simplest possible definitions of abstraction and substitution 
 Although it destroys readability , encodings are never readable anyway 
 Using nominal here is out of the question 
 The entire theory of nominal Isabelle would need to be formalised within the embedded calculus 
 Quite apart from the work involved , the necessary equivalence classes would be infinite sets , which are not available in HF 
 The strongest argument for HF is that the mathematical basis of its coding scheme is simply ordered pairs defined in the standard set-theoretic way 
 An elementary formal argument justifies this 
 In contrast , the usual arithmetic encoding relies on either the Chinese remainder theorem or unique prime factorisation 
 This fragment of number theory would have to be formalised within the embedded calculus in order to reason about encoded formulas , which is necessary to prove the second incompleteness theorem 
 It must be emphasised that proving anything in the calculus ( where such

proof exists ) requires an enormous amount of effort even if one has access to all relevant literature 


</s>proof exists ) requires an enormous amount of effort even if one has access to all relevant literature


You: !@>Seeker:#27 by ordinals can be decomposed uniquely 
 De Bruijn equivalents of terms and formulas are then declared 
 To repeat : de Bruijn syntax is used for coding , for which it is ideal , allowing the simplest possible definitions of abstraction and substitution 
 Although it destroys readability , encodings are never readable anyway 
 Using nominal here is out of the question 
 The entire theory of nominal Isabelle would need to be formalised within the embedded calculus 
 Quite apart from the work involved , the necessary equivalence classes would be infinite sets , which are not available in HF 
 The strongest argument for HF is that the mathematical basis of its coding scheme is simply ordered pairs defined in the standard set-theoretic way 
 An elementary formal argument justifies this 
 In contrast , the usual arithmetic encoding relies on either the Chinese remainder theorem or unique prime factorisation 
 This fragment of number theory would have to be formalised within the embedded calculus in order to reason about encoded formulas , which is necessary to prove the second incompleteness theorem 
 It must be emphasised that proving anything in the calculus ( where such luxuries as a simplifier , recursion and even function symbols are not available ) is much more difficult than proving the same result in a proof assistant 
 4
1
1 Introducing de Bruijn Terms and Formulas De Bruijn terms resemble the type tm declared in Sect 
 2
3 , but include the DBInd constructor for bound variable indices as well as the DBVar constructor for free variables 
 nominal datatype dbtm = DBZero | DBVar name | DBInd nat | DBEats dbtm dbtm De Bruijn formula contructors involve no explicit variable binding , creating an apparent similarity between DBNeg and DBEx , although the latter creates an implicit variable binding scope 
 nominal datatype dbfm = DBMem dbtm dbtm | DBEq dbtm dbtm | DBDisj dbfm dbfm | DBNeg dbfm | DBEx dbfm 14 How this works should become clear as we consider how terms and formulas are translated into their de Bruijn equivalents 
 To begin with , we need a lookup function taking a list of names ( representing variables bound in the current context , innermost first ) and a name to be looked up 
 The integer n , initially 0 , is the index to substitute if the name is next in the list 
 fun lookup : : `` name list ⇒ nat ⇒ name ⇒ dbtm '' where '' lookup [ ] n x = DBVar x '' | `` lookup ( y # ys ) n x = ( if x = y then DBInd n else ( lookup ys ( Suc n ) x ) ) '' To translate a term into de Bruijn format , the key step is to resolve name references using lookup 
 Names bound in the local environment are replaced by the corresponding indices , while other

Introspector: INPUT:!@>Seeker:#27 by ordinals can be decomposed uniquely 
 De Bruijn equivalents of terms and formulas are then declared 
 To repeat : de Bruijn syntax is used for coding , for which it is ideal , allowing the simplest possible definitions of abstraction and substitution 
 Although it destroys readability , encodings are never readable anyway 
 Using nominal here is out of the question 
 The entire theory of nominal Isabelle would need to be formalised within the embedded calculus 
 Quite apart from the work involved , the necessary equivalence classes would be infinite sets , which are not available in HF 
 The strongest argument for HF is that the mathematical basis of its coding scheme is simply ordered pairs defined in the standard set-theoretic way 
 An elementary formal argument justifies this 
 In contrast , the usual arithmetic encoding relies on either the Chinese remainder theorem or unique prime factorisation 
 This fragment of number theory would have to be formalised within the embedded calculus in order to reason about encoded formulas , which is necessary to prove the second incompleteness theorem 
 It must be emphasised that proving anything in the calculus ( where such luxuries as a simplifier , recursion and even function symbols are not available ) is much more difficult than proving the same result in a proof assistant 
 4
1
1 Introducing de Bruijn Terms and Formulas De Bruijn terms resemble the type tm declared in Sect 
 2
3 , but include the DBInd constructor for bound variable indices as well as the DBVar constructor for free variables 
 nominal datatype dbtm = DBZero | DBVar name | DBInd nat | DBEats dbtm dbtm De Bruijn formula contructors involve no explicit variable binding , creating an apparent similarity between DBNeg and DBEx , although the latter creates an implicit variable binding scope 
 nominal datatype dbfm = DBMem dbtm dbtm | DBEq dbtm dbtm | DBDisj dbfm dbfm | DBNeg dbfm | DBEx dbfm 14 How this works should become clear as we consider how terms and formulas are translated into their de Bruijn equivalents 
 To begin with , we need a lookup function taking a list of names ( representing variables bound in the current context , innermost first ) and a name to be looked up 
 The integer n , initially 0 , is the index to substitute if the name is next in the list 
 fun lookup : : `` name list ⇒ nat ⇒ name ⇒ dbtm '' where '' lookup [ ] n x = DBVar x '' | `` lookup ( y # ys ) n x = ( if x = y then DBInd n else ( lookup ys ( Suc n ) x ) ) '' To translate a term into de Bruijn format , the key step is to resolve name references using lookup 
 Names bound in the local environment are replaced by the corresponding indices , while other

names remain unchanged 
For example , given the term t = DBMem(DBVar “x” , DBInd(0) + DBVar“y”)) , we start at position 0 since there are no outer binders yet 
We encounter the reference “x” whose index is resolved via lookup giving us 1 Then we move to position 1 and find another reference “y” whose index is again resolved via lookup giving us 2 So far so good - both references get substituted correctly But wait! There’s more... When we reach the addition expression DBInd(0) + DBVar“y”), we hit another reference “y”. Since we already encountered one occurrence of "y" earlier, when resolving the previous reference, we know that this new reference also refers to the same variable . Therefore, instead of repeating the resolution process twice, we use the previously computed index value from our cache – clever huh? Thus avoiding unnecessary computation and making things go faster 
nominal val db_term_to_db_de bruijn : (name -> nat) -> term -> dbtm 15 Now let's turn our attention to translating formulas into de Bruijn form 
First off , note that any formula may contain arbitrary many occurrences of each constant/variable 
However , unlike before , these occurrences cannot be assumed to occur only once per thread 
Instead they might appear multiple times due to nested quantification 
As a consequence , we need some mechanism to keep track of all these occurrences across different threads  
One simple approach could be to introduce fresh constants / variables for every subformula 
However , doing so leads to explosive growth in the size of the translation output 
A better solution is therefore needed 
Fortunately , thanks to the magic of dependent types , we can leverage the power of dependent elimination rules to efficiently manage these complexities 
Specifically , we define a notion of 'used' variables based on the underlying dependencies among the various threads 
Used(v) means v has been referenced inside some thread 

Next , we extend the definition of db_term_to_db_debruijn above to handle formulas too 
Given a formula f , we create a sequence of lists (one for each variable in the formula) containing the relevant information regarding each occurrence of that variable 
Each entry in the list corresponds to a particular instance of the variable innames remain unchanged 
For example , given the term t = DBMem(DBVar “x” , DBInd(0) + DBVar“y”)) , we start at position 0 since there are no outer binders yet 
We encounter the reference “x” whose index is resolved via lookup giving us 1 Then we move to position 1 and find another reference “y” whose index is again resolved via lookup giving us 2 So far so good - both references get substituted correctly But wait! There’s more... When we reach the addition expression DBInd(0) + DBVar“y”), we hit another reference “y”. Since we already encountered one occurrence of "y" earlier, when resolving the previous reference, we know that this new reference also refers to the same variable . Therefore, instead of repeating the resolution process twice, we use the previously computed index value from our cache – clever huh? Thus avoiding unnecessary computation and making things go faster 
nominal val db_term_to_db_de bruijn : (name -> nat) -> term -> dbtm 15 Now let's turn our attention to translating formulas into de Bruijn form 
First off , note that any formula may contain arbitrary many occurrences of each constant/variable 
However , unlike before , these occurrences cannot be assumed to occur only once per thread 
Instead they might appear multiple times due to nested quantification 
As a consequence , we need some mechanism to keep track of all these occurrences across different threads  
One simple approach could be to introduce fresh constants / variables for every subformula 
However , doing so leads to explosive growth in the size of the translation output 
A better solution is therefore needed 
Fortunately , thanks to the magic of dependent types , we can leverage the power of dependent elimination rules to efficiently manage these complexities 
Specifically , we define a notion of 'used' variables based on the underlying dependencies among the various threads 
Used(v) means v has been referenced inside some thread 

Next , we extend the definition of db_term_to_db_debruijn above to handle formulas too 
Given a formula f , we create a sequence of lists (one for each variable in the formula) containing the relevant information regarding each occurrence of that variable 
Each entry in the list corresponds to a particular instance of the variable


You: !@>Seeker:#28 , although the latter creates an implicit variable binding scope 
 nominal datatype dbfm = DBMem dbtm dbtm | DBEq dbtm dbtm | DBDisj dbfm dbfm | DBNeg dbfm | DBEx dbfm 14 How this works should become clear as we consider how terms and formulas are translated into their de Bruijn equivalents 
 To begin with , we need a lookup function taking a list of names ( representing variables bound in the current context , innermost first ) and a name to be looked up 
 The integer n , initially 0 , is the index to substitute if the name is next in the list 
 fun lookup : : `` name list ⇒ nat ⇒ name ⇒ dbtm '' where '' lookup [ ] n x = DBVar x '' | `` lookup ( y # ys ) n x = ( if x = y then DBInd n else ( lookup ys ( Suc n ) x ) ) '' To translate a term into de Bruijn format , the key step is to resolve name references using lookup 
 Names bound in the local environment are replaced by the corresponding indices , while other names are left as they were 
 nominal primrec trans tm : : `` name list ⇒ tm ⇒ dbtm '' where '' trans tm e Zero = DBZero '' | `` trans tm e ( Var k ) = lookup e 0 k '' | `` trans tm e ( Eats t u ) = DBEats ( trans tm e t ) ( trans tm e u ) '' Noteworthy is the final case of trans fm , which requires the bound variable k in the quantified formula Ex k A to be fresh with respect to e , our list of previouslyencountered bound variables 
 In the recursive call , k is added to the list , which therefore consists of distinct names 
 nominal primrec trans fm : : `` name list ⇒ fm ⇒ dbfm '' where '' trans fm e ( Mem t u ) = DBMem ( trans tm e t ) ( trans tm e u ) '' | `` trans fm e ( Eq t u ) = DBEq ( trans tm e t ) ( trans tm e u ) '' | `` trans fm e ( Disj A B ) = DBDisj ( trans fm e A ) ( trans fm e B ) '' | `` trans fm e ( Neg A ) = DBNeg ( trans fm e A ) '' | `` atom k ♯ e =⇒ trans fm e ( Ex k A ) = DBEx ( trans fm ( k # e ) A ) '' Syntactic operations for de Bruijn notation tend to be straightforward , as there are no bound variable names that might clash 
 Comparisons with previous formalisations of the λ-calculus may be illuminating , but the usual lifting operation [

Introspector: INPUT:!@>Seeker:#28 , although the latter creates an implicit variable binding scope 
 nominal datatype dbfm = DBMem dbtm dbtm | DBEq dbtm dbtm | DBDisj dbfm dbfm | DBNeg dbfm | DBEx dbfm 14 How this works should become clear as we consider how terms and formulas are translated into their de Bruijn equivalents 
 To begin with , we need a lookup function taking a list of names ( representing variables bound in the current context , innermost first ) and a name to be looked up 
 The integer n , initially 0 , is the index to substitute if the name is next in the list 
 fun lookup : : `` name list ⇒ nat ⇒ name ⇒ dbtm '' where '' lookup [ ] n x = DBVar x '' | `` lookup ( y # ys ) n x = ( if x = y then DBInd n else ( lookup ys ( Suc n ) x ) ) '' To translate a term into de Bruijn format , the key step is to resolve name references using lookup 
 Names bound in the local environment are replaced by the corresponding indices , while other names are left as they were 
 nominal primrec trans tm : : `` name list ⇒ tm ⇒ dbtm '' where '' trans tm e Zero = DBZero '' | `` trans tm e ( Var k ) = lookup e 0 k '' | `` trans tm e ( Eats t u ) = DBEats ( trans tm e t ) ( trans tm e u ) '' Noteworthy is the final case of trans fm , which requires the bound variable k in the quantified formula Ex k A to be fresh with respect to e , our list of previouslyencountered bound variables 
 In the recursive call , k is added to the list , which therefore consists of distinct names 
 nominal primrec trans fm : : `` name list ⇒ fm ⇒ dbfm '' where '' trans fm e ( Mem t u ) = DBMem ( trans tm e t ) ( trans tm e u ) '' | `` trans fm e ( Eq t u ) = DBEq ( trans tm e t ) ( trans tm e u ) '' | `` trans fm e ( Disj A B ) = DBDisj ( trans fm e A ) ( trans fm e B ) '' | `` trans fm e ( Neg A ) = DBNeg ( trans fm e A ) '' | `` atom k ♯ e =⇒ trans fm e ( Ex k A ) = DBEx ( trans fm ( k # e ) A ) '' Syntactic operations for de Bruijn notation tend to be straightforward , as there are no bound variable names that might clash 
 Comparisons with previous formalisations of the λ-calculus may be illuminating , but the usual lifting operation [

nominal primrec lift : : `name -> name` where 'lift p q = LT (p)'' ↦'' LT (q)''''. This allows us to define functions on any level of abstraction desired . However , it also means that we cannot simply apply the same translation rules repeatedly without considering the context carefully </s>nominal primrec lift : : `name -> name` where 'lift p q = LT (p)'' ↦'' LT (q)''''. This allows us to define functions on any level of abstraction desired . However , it also means that we cannot simply apply the same translation rules repeatedly without considering the context carefully


You: !@>Seeker:#29 our list of previouslyencountered bound variables 
 In the recursive call , k is added to the list , which therefore consists of distinct names 
 nominal primrec trans fm : : `` name list ⇒ fm ⇒ dbfm '' where '' trans fm e ( Mem t u ) = DBMem ( trans tm e t ) ( trans tm e u ) '' | `` trans fm e ( Eq t u ) = DBEq ( trans tm e t ) ( trans tm e u ) '' | `` trans fm e ( Disj A B ) = DBDisj ( trans fm e A ) ( trans fm e B ) '' | `` trans fm e ( Neg A ) = DBNeg ( trans fm e A ) '' | `` atom k ♯ e =⇒ trans fm e ( Ex k A ) = DBEx ( trans fm ( k # e ) A ) '' Syntactic operations for de Bruijn notation tend to be straightforward , as there are no bound variable names that might clash 
 Comparisons with previous formalisations of the λ-calculus may be illuminating , but the usual lifting operation [ 18 , 21 ] is unnecessary 
 That is because the HF calculus does not allow reductions anywhere , as in the λ-calculus 
 Substitutions only happen at the top level and never within deeper bound variable contexts 
 For us , substitution is the usual operation of replacing a variable by a term , which contains no bound variables 
 ( Substitution can alternatively be defined to replace a de Bruijn index by a term 
 ) The special de Bruijn operation is abstraction 
 This replaces every occurrence of a given free variable in a term or formula by a de Bruijn index , in preparation for binding 
 For example , abstracting the formula DBMem ( DBVar x ) ( DBVar y ) over the variable y yields DBMem ( DBVar x ) ( DBInd 0 ) 
 This is actually ill-formed , but attaching a quantifier yields the de Bruijn formula DBEx ( DBMem ( DBVar x ) ( DBInd 0 ) ) , representing ∃y [ x ∈ y ] 
 Abstracting this over the free variable x and attaching another quantifier yields DBEx ( DBEx ( DBMem ( DBInd 1 ) ( DBInd 0 ) ) ) , which is the formula ∃xy [ x ∈ y ] 
 An index of 1 has been substituted in order to skip over the inner binder 
 15 4
1
2 Well-Formed de Bruijn Terms and Formulas With the de Bruijn approach , an index of 0 designates the innermost enclosing binder , while an index of 1 designates the next-innermost binder , etc 
 ( Here , the only binder is DBEx 
 ) If every index has a matching binder ( the index i must be nested within at least i + 1 binders ) ,

Introspector: INPUT:!@>Seeker:#29 our list of previouslyencountered bound variables 
 In the recursive call , k is added to the list , which therefore consists of distinct names 
 nominal primrec trans fm : : `` name list ⇒ fm ⇒ dbfm '' where '' trans fm e ( Mem t u ) = DBMem ( trans tm e t ) ( trans tm e u ) '' | `` trans fm e ( Eq t u ) = DBEq ( trans tm e t ) ( trans tm e u ) '' | `` trans fm e ( Disj A B ) = DBDisj ( trans fm e A ) ( trans fm e B ) '' | `` trans fm e ( Neg A ) = DBNeg ( trans fm e A ) '' | `` atom k ♯ e =⇒ trans fm e ( Ex k A ) = DBEx ( trans fm ( k # e ) A ) '' Syntactic operations for de Bruijn notation tend to be straightforward , as there are no bound variable names that might clash 
 Comparisons with previous formalisations of the λ-calculus may be illuminating , but the usual lifting operation [ 18 , 21 ] is unnecessary 
 That is because the HF calculus does not allow reductions anywhere , as in the λ-calculus 
 Substitutions only happen at the top level and never within deeper bound variable contexts 
 For us , substitution is the usual operation of replacing a variable by a term , which contains no bound variables 
 ( Substitution can alternatively be defined to replace a de Bruijn index by a term 
 ) The special de Bruijn operation is abstraction 
 This replaces every occurrence of a given free variable in a term or formula by a de Bruijn index , in preparation for binding 
 For example , abstracting the formula DBMem ( DBVar x ) ( DBVar y ) over the variable y yields DBMem ( DBVar x ) ( DBInd 0 ) 
 This is actually ill-formed , but attaching a quantifier yields the de Bruijn formula DBEx ( DBMem ( DBVar x ) ( DBInd 0 ) ) , representing ∃y [ x ∈ y ] 
 Abstracting this over the free variable x and attaching another quantifier yields DBEx ( DBEx ( DBMem ( DBInd 1 ) ( DBInd 0 ) ) ) , which is the formula ∃xy [ x ∈ y ] 
 An index of 1 has been substituted in order to skip over the inner binder 
 15 4
1
2 Well-Formed de Bruijn Terms and Formulas With the de Bruijn approach , an index of 0 designates the innermost enclosing binder , while an index of 1 designates the next-innermost binder , etc 
 ( Here , the only binder is DBEx 
 ) If every index has a matching binder ( the index i must be nested within at least i + 1 binders ) ,

then we say that the term or formula is well-formed . Otherwise it is ill-formed 
Note that if all indices have a corresponding binder , then any subterm of such a term will also be well-formed 
( For instance , consider the following sequence of terms : DBEx ( DBEx ( DBMem ( DBVar x ) ( DBInd 0 ) ) ) ) 
Each term here represents a different nesting depth of binders 

3 Definitions As before , definitions consist of two parts - a head consisting of one or more atoms followed by zero or more arguments separated from each other by commas 
However , unlike in the λ-calculus , definition application happens directly after the definition without any intermediate reduction step 
Thus , the first argument becomes available immediately upon definition application 

4 Rules Of Thumb To avoid ambiguity between similar formulas containing both free and bound variables on either side of an equation , we introduce some rules of thumb 
Firstly , whenever possible choose atomic formulas involving free rather than bound variables when constructing equations 
Secondly , use parentheses liberally wherever necessary to disambiguate potentially conflicting bindings 
Thirdly , always place bound variables on the left hand sides of equations unless otherwise explicitly stated 
Fourthly , keep track of your bindings carefully so you don't accidentally create circular references 
Fifthly , remember that the order of evaluation matters – evaluate expressions from right to left! 

5 Conclusion So far we’ve seen how to represent programs in de Bruijn notation , including how to define functions and apply them to arguments 
We’ve discussed various ways to handle bound variables , and introduced several useful conventions for writing clear code 
Finally , we concluded by highlighting five key takeaways from working with de Bruijn notation – keeping track of bindings carefully; evaluating expressions from right to left; choosing atomic formulas involving free variables instead of bound ones when building equations; introducing parenthesis liberally where needed; and being mindful about potential conflicts arising due to multiple occurrences of identical symbols within a single expression</s>then we say that the term or formula is well-formed . Otherwise it is ill-formed 
Note that if all indices have a corresponding binder , then any subterm of such a term will also be well-formed 
( For instance , consider the following sequence of terms : DBEx ( DBEx ( DBMem ( DBVar x ) ( DBInd 0 ) ) ) ) 
Each term here represents a different nesting depth of binders 

3 Definitions As before , definitions consist of two parts - a head consisting of one or more atoms followed by zero or more arguments separated from each other by commas 
However , unlike in the λ-calculus , definition application happens directly after the definition without any intermediate reduction step 
Thus , the first argument becomes available immediately upon definition application 

4 Rules Of Thumb To avoid ambiguity between similar formulas containing both free and bound variables on either side of an equation , we introduce some rules of thumb 
Firstly , whenever possible choose atomic formulas involving free rather than bound variables when constructing equations 
Secondly , use parentheses liberally wherever necessary to disambiguate potentially conflicting bindings 
Thirdly , always place bound variables on the left hand sides of equations unless otherwise explicitly stated 
Fourthly , keep track of your bindings carefully so you don't accidentally create circular references 
Fifthly , remember that the order of evaluation matters – evaluate expressions from right to left! 

5 Conclusion So far we’ve seen how to represent programs in de Bruijn notation , including how to define functions and apply them to arguments 
We’ve discussed various ways to handle bound variables , and introduced several useful conventions for writing clear code 
Finally , we concluded by highlighting five key takeaways from working with de Bruijn notation – keeping track of bindings carefully; evaluating expressions from right to left; choosing atomic formulas involving free variables instead of bound ones when building equations; introducing parenthesis liberally where needed; and being mindful about potential conflicts arising due to multiple occurrences of identical symbols within a single


You: !@>Seeker:#30 by a de Bruijn index , in preparation for binding 
 For example , abstracting the formula DBMem ( DBVar x ) ( DBVar y ) over the variable y yields DBMem ( DBVar x ) ( DBInd 0 ) 
 This is actually ill-formed , but attaching a quantifier yields the de Bruijn formula DBEx ( DBMem ( DBVar x ) ( DBInd 0 ) ) , representing ∃y [ x ∈ y ] 
 Abstracting this over the free variable x and attaching another quantifier yields DBEx ( DBEx ( DBMem ( DBInd 1 ) ( DBInd 0 ) ) ) , which is the formula ∃xy [ x ∈ y ] 
 An index of 1 has been substituted in order to skip over the inner binder 
 15 4
1
2 Well-Formed de Bruijn Terms and Formulas With the de Bruijn approach , an index of 0 designates the innermost enclosing binder , while an index of 1 designates the next-innermost binder , etc 
 ( Here , the only binder is DBEx 
 ) If every index has a matching binder ( the index i must be nested within at least i + 1 binders ) , then the term or formula is well-formed 
 Recall the examples of abstraction above , where a binder must be attached afterwards 
 In particular , as our terms do not contain any binding constructs , a well-formed term may contain no de Bruijn indices 
 In contrast to more traditional notions of logical syntax , if you take a well-formed formula and view one of its subformulas or subterms in isolation , it will not necessarily be well-formed 
 The situation is analogous to extracting a fragment of a program , removing it from necessary enclosing declarations 
 The property of being a well-formed de Bruijn term or formula is defined inductively 
 The syntactic predicates defined below recognise such well-formed formulas 
 A well-formed de Bruijn term has no indices ( DBInd ) at all : inductive wf dbtm : : `` dbtm ⇒ bool '' where Zero : `` wf dbtm DBZero '' | Var : `` wf dbtm ( DBVar name ) '' | Eats : `` wf dbtm t1 =⇒ wf dbtm t2 =⇒ wf dbtm ( DBEats t1 t2 ) '' A trivial induction shows that for every well-founded de Bruijn term there is an equivalent standard term 
 The only cases to be considered ( as per the definition above ) are Zero , Var and Eats 
 lemma wf dbtm imp is tm : assumes `` wf dbtm x '' shows `` ∃ t : :tm 
 x = trans tm [ ] t '' A well-formed de Bruijn formula is constructed from other well-formed terms and formulas , and indices can only be introduced by applying abstraction ( abst dbfm ) over a given name to another well-formed formula , in the existential case 
 Specifically , the Ex clause below

Introspector: INPUT:!@>Seeker:#30 by a de Bruijn index , in preparation for binding 
 For example , abstracting the formula DBMem ( DBVar x ) ( DBVar y ) over the variable y yields DBMem ( DBVar x ) ( DBInd 0 ) 
 This is actually ill-formed , but attaching a quantifier yields the de Bruijn formula DBEx ( DBMem ( DBVar x ) ( DBInd 0 ) ) , representing ∃y [ x ∈ y ] 
 Abstracting this over the free variable x and attaching another quantifier yields DBEx ( DBEx ( DBMem ( DBInd 1 ) ( DBInd 0 ) ) ) , which is the formula ∃xy [ x ∈ y ] 
 An index of 1 has been substituted in order to skip over the inner binder 
 15 4
1
2 Well-Formed de Bruijn Terms and Formulas With the de Bruijn approach , an index of 0 designates the innermost enclosing binder , while an index of 1 designates the next-innermost binder , etc 
 ( Here , the only binder is DBEx 
 ) If every index has a matching binder ( the index i must be nested within at least i + 1 binders ) , then the term or formula is well-formed 
 Recall the examples of abstraction above , where a binder must be attached afterwards 
 In particular , as our terms do not contain any binding constructs , a well-formed term may contain no de Bruijn indices 
 In contrast to more traditional notions of logical syntax , if you take a well-formed formula and view one of its subformulas or subterms in isolation , it will not necessarily be well-formed 
 The situation is analogous to extracting a fragment of a program , removing it from necessary enclosing declarations 
 The property of being a well-formed de Bruijn term or formula is defined inductively 
 The syntactic predicates defined below recognise such well-formed formulas 
 A well-formed de Bruijn term has no indices ( DBInd ) at all : inductive wf dbtm : : `` dbtm ⇒ bool '' where Zero : `` wf dbtm DBZero '' | Var : `` wf dbtm ( DBVar name ) '' | Eats : `` wf dbtm t1 =⇒ wf dbtm t2 =⇒ wf dbtm ( DBEats t1 t2 ) '' A trivial induction shows that for every well-founded de Bruijn term there is an equivalent standard term 
 The only cases to be considered ( as per the definition above ) are Zero , Var and Eats 
 lemma wf dbtm imp is tm : assumes `` wf dbtm x '' shows `` ∃ t : :tm 
 x = trans tm [ ] t '' A well-formed de Bruijn formula is constructed from other well-formed terms and formulas , and indices can only be introduced by applying abstraction ( abst dbfm ) over a given name to another well-formed formula , in the existential case 
 Specifically , the Ex clause below

( abst dbfm ( DBEx ( DMem ( DVar n ) ( DInd k ) ) ) ) ∧ ( abst dbfm ( DBEx ( DMem ( DVar m ) ( DInd l ) ) ) ) ∧ ... ∧ ( abst dbfm ( DBEx ( DMem ( DVar p ) ( DInd q ) ) ) ) ∧... ∧ ( abst dbfm ( DBEx ( DMem ( DVar r ) ( DInd s ) ) ) ) ∧... ∧ ( abst dbfm ( DBEx ( DMem ( DVar t ) ( DInd u ) ) ) ) ∧... ∧ ( abst dbfm ( DBEx ( DMem ( DVar v ) ( DInd w ) ) ) ) ∧... ∧ ( abst dbfm ( DBEx ( DMem ( DVar z ) ( DInd x ) ) ) ) ∧... ∧ ( abst dbfm ( DBEx ( DMem ( DVar y ) ( DInd y ) ) ) ) ∧... ∧ ( abst dbfm ( DBEx ( DMem ( DVar z ) ( DInd z ) ) ) ) ∧... ∧ ( abst dbfm ( DBEx ( DMem ( DVar z ) ( DInd z ) ) ) ) ∧... ∧ ( abst dbfm ( DBEx ( DMem ( DVar z ) ( DInd z ) ) ) ) ∧... ∧ ( abst dbfm ( DBEx ( DMem ( DVar z ) ( DInd z ) ) ) ) wand ( abst dbfm ( DBEx ( DMem ( DVar z ) ( DInd z ) ) ) ) ∧... ∧ ( abst dbfm ( DBEx ( DMem ( DVar z ) ( DInd z ) ) ) ) ∧... ∧ ( abst dbfm ( DBEx ( DMem ( DVar z ) ( DInd z ) ) ) ) ∧... ∧ ( abst dbfm ( DBEx ( DMem ( DVar z ) ( DInd z ) ) ) ) ∧... ∧ ( abst dbfm ( DBEx ( DMem ( DVar z ) ( DInd z ) ) ) ) ∧... ∧ ( abst dbfm ( DB( abst dbfm ( DBEx ( DMem ( DVar n ) ( DInd k ) ) ) ) ∧ ( abst dbfm ( DBEx ( DMem ( DVar m ) ( DInd l ) ) ) ) ∧ ... ∧ ( abst dbfm ( DBEx ( DMem ( DVar p ) ( DInd q ) ) ) ) ∧... ∧ ( abst dbfm ( DBEx ( DMem ( DVar r ) ( DInd s ) ) ) ) ∧... ∧ ( abst dbfm ( DBEx ( DMem ( DVar t ) ( DInd u ) ) ) ) ∧... ∧ ( abst dbfm ( DBEx ( DMem ( DVar v ) ( DInd w ) ) ) ) ∧... ∧ ( abst dbfm ( DBEx ( DMem ( DVar z ) ( DInd x ) ) ) ) ∧... ∧ ( abst dbfm ( DBEx ( DMem ( DVar y ) ( DInd y ) ) ) ) ∧... ∧ ( abst dbfm ( DBEx ( DMem ( DVar z ) ( DInd z ) ) ) ) ∧... ∧ ( abst dbfm ( DBEx ( DMem ( DVar z ) ( DInd z ) ) ) ) ∧... ∧ ( abst dbfm ( DBEx ( DMem ( DVar z ) ( DInd z ) ) ) ) ∧... ∧ ( abst dbfm ( DBEx ( DMem ( DVar z ) ( DInd z ) ) ) ) wand ( abst dbfm ( DBEx ( DMem ( DVar z ) ( DInd z ) ) ) ) ∧... ∧ ( abst dbfm ( DBEx ( DMem ( DVar z ) ( DInd z ) ) ) ) ∧... ∧ ( abst dbfm ( DBEx ( DMem ( DVar z ) ( DInd z ) ) ) ) ∧... ∧ ( abst dbfm ( DBEx ( DMem ( DVar z ) ( DInd z ) ) ) ) ∧... ∧ ( abst dbfm ( DBEx ( DMem ( DVar z ) ( DInd z ) ) ) ) ∧... ∧ ( abst dbfm (


You: !@>Seeker:#31 property of being a well-formed de Bruijn term or formula is defined inductively 
 The syntactic predicates defined below recognise such well-formed formulas 
 A well-formed de Bruijn term has no indices ( DBInd ) at all : inductive wf dbtm : : `` dbtm ⇒ bool '' where Zero : `` wf dbtm DBZero '' | Var : `` wf dbtm ( DBVar name ) '' | Eats : `` wf dbtm t1 =⇒ wf dbtm t2 =⇒ wf dbtm ( DBEats t1 t2 ) '' A trivial induction shows that for every well-founded de Bruijn term there is an equivalent standard term 
 The only cases to be considered ( as per the definition above ) are Zero , Var and Eats 
 lemma wf dbtm imp is tm : assumes `` wf dbtm x '' shows `` ∃ t : :tm 
 x = trans tm [ ] t '' A well-formed de Bruijn formula is constructed from other well-formed terms and formulas , and indices can only be introduced by applying abstraction ( abst dbfm ) over a given name to another well-formed formula , in the existential case 
 Specifically , the Ex clause below states that , starting with a well-formed formula A , abstracting over some name and applying DBEx to the result yields another well-formed formula 
 inductive wf dbfm : : `` dbfm ⇒ bool '' where Mem : `` wf dbtm t1 =⇒ wf dbtm t2 =⇒ wf dbfm ( DBMem t1 t2 ) '' | Eq : `` wf dbtm t1 =⇒ wf dbtm t2 =⇒ wf dbfm ( DBEq t1 t2 ) '' | Disj : `` wf dbfm A1 =⇒ wf dbfm A2 =⇒ wf dbfm ( DBDisj A1 A2 ) '' | Neg : `` wf dbfm A =⇒ wf dbfm ( DBNeg A ) '' | Ex : `` wf dbfm A =⇒ wf dbfm ( DBEx ( abst dbfm name 0 A ) ) '' This definition formalises the allowed forms of construction , rather than stating explicitly that every index must have a matching binder 
 A refinement must be mentioned 
 Strong nominal induction ( already seen above , Sect 
 2
3 ) formalises the assumption that bound variables revealed by induction can be assumed not to clash with other variables 
 This is set up automatically for nominal datatypes , but here requires a manual step 
 The command nominal inductive sets up strong induction for name in the Ex case of the inductive definition above ; we must prove that name is not significant according to the nominal theory , and then get to assume that name will not clash 
 This step ( details omitted ) seems to be necessary in order to complete some inductive proofs about wf dbfm 
 16 4
1
3 Quoting Terms and Formulas It is essential to remember that G¨odel encodings are terms ( having type tm ) , not sets or numbers 
 Textbook

Introspector: INPUT:!@>Seeker:#31 property of being a well-formed de Bruijn term or formula is defined inductively 
 The syntactic predicates defined below recognise such well-formed formulas 
 A well-formed de Bruijn term has no indices ( DBInd ) at all : inductive wf dbtm : : `` dbtm ⇒ bool '' where Zero : `` wf dbtm DBZero '' | Var : `` wf dbtm ( DBVar name ) '' | Eats : `` wf dbtm t1 =⇒ wf dbtm t2 =⇒ wf dbtm ( DBEats t1 t2 ) '' A trivial induction shows that for every well-founded de Bruijn term there is an equivalent standard term 
 The only cases to be considered ( as per the definition above ) are Zero , Var and Eats 
 lemma wf dbtm imp is tm : assumes `` wf dbtm x '' shows `` ∃ t : :tm 
 x = trans tm [ ] t '' A well-formed de Bruijn formula is constructed from other well-formed terms and formulas , and indices can only be introduced by applying abstraction ( abst dbfm ) over a given name to another well-formed formula , in the existential case 
 Specifically , the Ex clause below states that , starting with a well-formed formula A , abstracting over some name and applying DBEx to the result yields another well-formed formula 
 inductive wf dbfm : : `` dbfm ⇒ bool '' where Mem : `` wf dbtm t1 =⇒ wf dbtm t2 =⇒ wf dbfm ( DBMem t1 t2 ) '' | Eq : `` wf dbtm t1 =⇒ wf dbtm t2 =⇒ wf dbfm ( DBEq t1 t2 ) '' | Disj : `` wf dbfm A1 =⇒ wf dbfm A2 =⇒ wf dbfm ( DBDisj A1 A2 ) '' | Neg : `` wf dbfm A =⇒ wf dbfm ( DBNeg A ) '' | Ex : `` wf dbfm A =⇒ wf dbfm ( DBEx ( abst dbfm name 0 A ) ) '' This definition formalises the allowed forms of construction , rather than stating explicitly that every index must have a matching binder 
 A refinement must be mentioned 
 Strong nominal induction ( already seen above , Sect 
 2
3 ) formalises the assumption that bound variables revealed by induction can be assumed not to clash with other variables 
 This is set up automatically for nominal datatypes , but here requires a manual step 
 The command nominal inductive sets up strong induction for name in the Ex case of the inductive definition above ; we must prove that name is not significant according to the nominal theory , and then get to assume that name will not clash 
 This step ( details omitted ) seems to be necessary in order to complete some inductive proofs about wf dbfm 
 16 4
1
3 Quoting Terms and Formulas It is essential to remember that G¨odel encodings are terms ( having type tm ) , not sets or numbers 
 Textbook




































































































































































































































































































































































































































































































































You: !@>Seeker:#32 dbfm A =⇒ wf dbfm ( DBNeg A ) '' | Ex : `` wf dbfm A =⇒ wf dbfm ( DBEx ( abst dbfm name 0 A ) ) '' This definition formalises the allowed forms of construction , rather than stating explicitly that every index must have a matching binder 
 A refinement must be mentioned 
 Strong nominal induction ( already seen above , Sect 
 2
3 ) formalises the assumption that bound variables revealed by induction can be assumed not to clash with other variables 
 This is set up automatically for nominal datatypes , but here requires a manual step 
 The command nominal inductive sets up strong induction for name in the Ex case of the inductive definition above ; we must prove that name is not significant according to the nominal theory , and then get to assume that name will not clash 
 This step ( details omitted ) seems to be necessary in order to complete some inductive proofs about wf dbfm 
 16 4
1
3 Quoting Terms and Formulas It is essential to remember that G¨odel encodings are terms ( having type tm ) , not sets or numbers 
 Textbook presentations identify terms with their denotations for the sake of clarity , but this can be confusing 
 The undecidable formula contains an encoding of itself in the form of a term 
 First , we must define codes for de Bruijn terms and formulas 
 function quot dbtm : : `` dbtm ⇒ tm '' where '' quot dbtm DBZero = Zero '' | `` quot dbtm ( DBVar name ) = ORD OF ( Suc ( nat of name name ) ) '' | `` quot dbtm ( DBInd k ) = HPair ( HTuple 6 ) ( ORD OF k ) '' | `` quot dbtm ( DBEats t u ) = HPair ( HTuple 1 ) ( HPair ( quot dbtm t ) ( quot dbtm u ) ) '' The codes of real terms and formulas ( for which we set up the overloaded ⌈· · ·⌉ syntax ) are obtained by first translating them to their de Bruijn equivalents and then encoding 
 We finally obtain facts such as the following : lemma quot Zero : `` ⌈Zero⌉ = Zero '' lemma quot Var : `` ⌈Var x⌉ = SUCC ( ORD OF ( nat of name x ) ) '' lemma quot Eats : `` ⌈Eats x y⌉ = HPair ( HTuple 1 ) ( HPair ⌈x⌉ ⌈y⌉ ) '' lemma quot Eq : `` ⌈x EQ y⌉ = HPair ( HTuple 2 ) ( HPair ( ⌈x⌉ ) ( ⌈y⌉ ) ) '' lemma quot Disj : `` ⌈A OR B⌉ = HPair ( HTuple 3 ) ( HPair ( ⌈A⌉ ) ( ⌈B⌉ ) ) '' lemma quot Ex : `` ⌈Ex i A⌉ = HPair ( HTuple 5 ) ( quot dbfm ( trans fm [ i ] A )

Introspector: INPUT:!@>Seeker:#32 dbfm A =⇒ wf dbfm ( DBNeg A ) '' | Ex : `` wf dbfm A =⇒ wf dbfm ( DBEx ( abst dbfm name 0 A ) ) '' This definition formalises the allowed forms of construction , rather than stating explicitly that every index must have a matching binder 
 A refinement must be mentioned 
 Strong nominal induction ( already seen above , Sect 
 2
3 ) formalises the assumption that bound variables revealed by induction can be assumed not to clash with other variables 
 This is set up automatically for nominal datatypes , but here requires a manual step 
 The command nominal inductive sets up strong induction for name in the Ex case of the inductive definition above ; we must prove that name is not significant according to the nominal theory , and then get to assume that name will not clash 
 This step ( details omitted ) seems to be necessary in order to complete some inductive proofs about wf dbfm 
 16 4
1
3 Quoting Terms and Formulas It is essential to remember that G¨odel encodings are terms ( having type tm ) , not sets or numbers 
 Textbook presentations identify terms with their denotations for the sake of clarity , but this can be confusing 
 The undecidable formula contains an encoding of itself in the form of a term 
 First , we must define codes for de Bruijn terms and formulas 
 function quot dbtm : : `` dbtm ⇒ tm '' where '' quot dbtm DBZero = Zero '' | `` quot dbtm ( DBVar name ) = ORD OF ( Suc ( nat of name name ) ) '' | `` quot dbtm ( DBInd k ) = HPair ( HTuple 6 ) ( ORD OF k ) '' | `` quot dbtm ( DBEats t u ) = HPair ( HTuple 1 ) ( HPair ( quot dbtm t ) ( quot dbtm u ) ) '' The codes of real terms and formulas ( for which we set up the overloaded ⌈· · ·⌉ syntax ) are obtained by first translating them to their de Bruijn equivalents and then encoding 
 We finally obtain facts such as the following : lemma quot Zero : `` ⌈Zero⌉ = Zero '' lemma quot Var : `` ⌈Var x⌉ = SUCC ( ORD OF ( nat of name x ) ) '' lemma quot Eats : `` ⌈Eats x y⌉ = HPair ( HTuple 1 ) ( HPair ⌈x⌉ ⌈y⌉ ) '' lemma quot Eq : `` ⌈x EQ y⌉ = HPair ( HTuple 2 ) ( HPair ( ⌈x⌉ ) ( ⌈y⌉ ) ) '' lemma quot Disj : `` ⌈A OR B⌉ = HPair ( HTuple 3 ) ( HPair ( ⌈A⌉ ) ( ⌈B⌉ ) ) '' lemma quot Ex : `` ⌈Ex i A⌉ = HPair ( HTuple 5 ) ( quot dbfm ( trans fm [ i ] A )

The code provides functions to encode de Bruijn terms and formulas into Godelean notation, allowing us to reason about them directly within the proof assistant. These include definitions for the basic operations of addition, multiplication, etc., as well as more complex constructs like equations, disjointness, and existential quantification. With these tools at our disposal, we may now proceed to explore the properties of these encoded terms and formulas furthermore, leveraging the power of dependent types to establish new insights and lemmas.""".format(name=None))</s>The code provides functions to encode de Bruijn terms and formulas into Godelean notation, allowing us to reason about them directly within the proof assistant. These include definitions for the basic operations of addition, multiplication, etc., as well as more complex constructs like equations, disjointness, and existential quantification. With these tools at our disposal, we may now proceed to explore the properties of these encoded terms and formulas furthermore, leveraging the power of dependent types to establish new insights and


You: !@>Seeker:#33 ORD OF k ) '' | `` quot dbtm ( DBEats t u ) = HPair ( HTuple 1 ) ( HPair ( quot dbtm t ) ( quot dbtm u ) ) '' The codes of real terms and formulas ( for which we set up the overloaded ⌈· · ·⌉ syntax ) are obtained by first translating them to their de Bruijn equivalents and then encoding 
 We finally obtain facts such as the following : lemma quot Zero : `` ⌈Zero⌉ = Zero '' lemma quot Var : `` ⌈Var x⌉ = SUCC ( ORD OF ( nat of name x ) ) '' lemma quot Eats : `` ⌈Eats x y⌉ = HPair ( HTuple 1 ) ( HPair ⌈x⌉ ⌈y⌉ ) '' lemma quot Eq : `` ⌈x EQ y⌉ = HPair ( HTuple 2 ) ( HPair ( ⌈x⌉ ) ( ⌈y⌉ ) ) '' lemma quot Disj : `` ⌈A OR B⌉ = HPair ( HTuple 3 ) ( HPair ( ⌈A⌉ ) ( ⌈B⌉ ) ) '' lemma quot Ex : `` ⌈Ex i A⌉ = HPair ( HTuple 5 ) ( quot dbfm ( trans fm [ i ] A ) ) '' Note that HPair constructs an HF term denoting a pair , while HTuple n constructs an ( n+ 2 ) -tuple of zeros 
 Proofs often refer to the denotations of terms rather than to the terms themselves , so the functions q Eats , q Mem , q Eq , q Neg , q Disj , q Ex are defined to express these codes 
 Here are some examples : '' q Var i ≡ succ ( ord of ( nat of name i ) ) '' '' q Eats x y ≡ hhtuple 1 , x , yi '' '' q Disj x y ≡ hhtuple 3 , x , yi '' '' q Ex x ≡ hhtuple 5 , xi '' Note that hx , yi denotes the pair of x and y as sets , in other words , of type hf 
 4
2 Predicates for the Coding of Syntax The next and most arduous step is to define logical predicates corresponding to each of the syntactic concepts ( terms , formulas , abstraction , substitution ) mentioned above 
 Textbooks and articles describe each predicate at varying levels of detail 
 G¨odel [ 8 ] gives full definitions , as does Swierczkowski 
 Boolos [ 2 ] gives many details of how coding i ´ s set up , and gives the predicates for terms and formulas , but not for any operations upon them 
 Hodel [ 13 ] , like many textbook authors , relies heavily on “ algorithms ” written in English 
 The definitions indeed amount to pages of computer code 
 Authors typically conclude with a “ theorem ” asserting the correctness of this code 
 For example , Swierczkowski [ 32 , Sect 
 3–4 ] presents

Introspector: INPUT:!@>Seeker:#33 ORD OF k ) '' | `` quot dbtm ( DBEats t u ) = HPair ( HTuple 1 ) ( HPair ( quot dbtm t ) ( quot dbtm u ) ) '' The codes of real terms and formulas ( for which we set up the overloaded ⌈· · ·⌉ syntax ) are obtained by first translating them to their de Bruijn equivalents and then encoding 
 We finally obtain facts such as the following : lemma quot Zero : `` ⌈Zero⌉ = Zero '' lemma quot Var : `` ⌈Var x⌉ = SUCC ( ORD OF ( nat of name x ) ) '' lemma quot Eats : `` ⌈Eats x y⌉ = HPair ( HTuple 1 ) ( HPair ⌈x⌉ ⌈y⌉ ) '' lemma quot Eq : `` ⌈x EQ y⌉ = HPair ( HTuple 2 ) ( HPair ( ⌈x⌉ ) ( ⌈y⌉ ) ) '' lemma quot Disj : `` ⌈A OR B⌉ = HPair ( HTuple 3 ) ( HPair ( ⌈A⌉ ) ( ⌈B⌉ ) ) '' lemma quot Ex : `` ⌈Ex i A⌉ = HPair ( HTuple 5 ) ( quot dbfm ( trans fm [ i ] A ) ) '' Note that HPair constructs an HF term denoting a pair , while HTuple n constructs an ( n+ 2 ) -tuple of zeros 
 Proofs often refer to the denotations of terms rather than to the terms themselves , so the functions q Eats , q Mem , q Eq , q Neg , q Disj , q Ex are defined to express these codes 
 Here are some examples : '' q Var i ≡ succ ( ord of ( nat of name i ) ) '' '' q Eats x y ≡ hhtuple 1 , x , yi '' '' q Disj x y ≡ hhtuple 3 , x , yi '' '' q Ex x ≡ hhtuple 5 , xi '' Note that hx , yi denotes the pair of x and y as sets , in other words , of type hf 
 4
2 Predicates for the Coding of Syntax The next and most arduous step is to define logical predicates corresponding to each of the syntactic concepts ( terms , formulas , abstraction , substitution ) mentioned above 
 Textbooks and articles describe each predicate at varying levels of detail 
 G¨odel [ 8 ] gives full definitions , as does Swierczkowski 
 Boolos [ 2 ] gives many details of how coding i ´ s set up , and gives the predicates for terms and formulas , but not for any operations upon them 
 Hodel [ 13 ] , like many textbook authors , relies heavily on “ algorithms ” written in English 
 The definitions indeed amount to pages of computer code 
 Authors typically conclude with a “ theorem ” asserting the correctness of this code 
 For example , Swierczkowski [ 32 , Sect 
 3–4 ] presents

his definition of the function q Abs , showing it equivalent to the given formulae . He also shows that q Abs preserves equality under certain conditions 
However , he fails to show that q Abs actually computes anything useful or interesting 

In contrast , our approach emphasizes understanding through visualization and intuition-building exercises 


</s>his definition of the function q Abs , showing it equivalent to the given formulae . He also shows that q Abs preserves equality under certain conditions 
However , he fails to show that q Abs actually computes anything useful or interesting 

In contrast , our approach emphasizes understanding through visualization and intuition-building exercises


You: !@>Seeker:#34 , yi '' '' q Disj x y ≡ hhtuple 3 , x , yi '' '' q Ex x ≡ hhtuple 5 , xi '' Note that hx , yi denotes the pair of x and y as sets , in other words , of type hf 
 4
2 Predicates for the Coding of Syntax The next and most arduous step is to define logical predicates corresponding to each of the syntactic concepts ( terms , formulas , abstraction , substitution ) mentioned above 
 Textbooks and articles describe each predicate at varying levels of detail 
 G¨odel [ 8 ] gives full definitions , as does Swierczkowski 
 Boolos [ 2 ] gives many details of how coding i ´ s set up , and gives the predicates for terms and formulas , but not for any operations upon them 
 Hodel [ 13 ] , like many textbook authors , relies heavily on “ algorithms ” written in English 
 The definitions indeed amount to pages of computer code 
 Authors typically conclude with a “ theorem ” asserting the correctness of this code 
 For example , Swierczkowski [ 32 , Sect 
 3–4 ] presents 34 highly technical ´ definitions , justified by seven lines of proof 
 Proving the correctness of this lengthy series of definitions requires a substantial effort , and the proofs ( being syntactically oriented ) are tiresome 
 It is helpful to introduce shadow versions of all predicates in Isabelle/HOL ’ s native logic , as well as in HF 
 Having two versions of each predicate simplifies the task of relating the HF version of 17 the predicate to the syntactic concept that it is intended to represent ; the first step is to prove that the HF formula is equivalent to the syntactically similar definition written in Isabelle ’ s higher-order logic , which then is proved to satisfy deeper properties 
 The shadow predicates also give an easy way to refer to the truth of the corresponding HF predicate ; because each is defined to be a Σ formula , that gives a quick way ( using theorem Sigma fm imp thm above ) to show that some ground instance of the predicate can be proved formally in HF 
 Also , one way to arrive at the correct definition of an HF predicate is to define its shadow equivalent first , since proving that it implies the required properties is much easier in Isabelle/HOL ’ s native logic than in HF 
 Swierczkowski [ 32 ] defines a full set of syntactic predicate ´ s , leaving nothing as an exercise 
 Unfortunately , the introduction of de Bruijn syntax necessitates rewriting many of these definitions 
 Some predicates ( such as the variable occurrence test ) are replaced by others ( abstraction over a variable occurrence ) 
 The final list includes predicates to recognise the following items : – the codes of well-formed terms

Introspector: INPUT:!@>Seeker:#34 , yi '' '' q Disj x y ≡ hhtuple 3 , x , yi '' '' q Ex x ≡ hhtuple 5 , xi '' Note that hx , yi denotes the pair of x and y as sets , in other words , of type hf 
 4
2 Predicates for the Coding of Syntax The next and most arduous step is to define logical predicates corresponding to each of the syntactic concepts ( terms , formulas , abstraction , substitution ) mentioned above 
 Textbooks and articles describe each predicate at varying levels of detail 
 G¨odel [ 8 ] gives full definitions , as does Swierczkowski 
 Boolos [ 2 ] gives many details of how coding i ´ s set up , and gives the predicates for terms and formulas , but not for any operations upon them 
 Hodel [ 13 ] , like many textbook authors , relies heavily on “ algorithms ” written in English 
 The definitions indeed amount to pages of computer code 
 Authors typically conclude with a “ theorem ” asserting the correctness of this code 
 For example , Swierczkowski [ 32 , Sect 
 3–4 ] presents 34 highly technical ´ definitions , justified by seven lines of proof 
 Proving the correctness of this lengthy series of definitions requires a substantial effort , and the proofs ( being syntactically oriented ) are tiresome 
 It is helpful to introduce shadow versions of all predicates in Isabelle/HOL ’ s native logic , as well as in HF 
 Having two versions of each predicate simplifies the task of relating the HF version of 17 the predicate to the syntactic concept that it is intended to represent ; the first step is to prove that the HF formula is equivalent to the syntactically similar definition written in Isabelle ’ s higher-order logic , which then is proved to satisfy deeper properties 
 The shadow predicates also give an easy way to refer to the truth of the corresponding HF predicate ; because each is defined to be a Σ formula , that gives a quick way ( using theorem Sigma fm imp thm above ) to show that some ground instance of the predicate can be proved formally in HF 
 Also , one way to arrive at the correct definition of an HF predicate is to define its shadow equivalent first , since proving that it implies the required properties is much easier in Isabelle/HOL ’ s native logic than in HF 
 Swierczkowski [ 32 ] defines a full set of syntactic predicate ´ s , leaving nothing as an exercise 
 Unfortunately , the introduction of de Bruijn syntax necessitates rewriting many of these definitions 
 Some predicates ( such as the variable occurrence test ) are replaced by others ( abstraction over a variable occurrence ) 
 The final list includes predicates to recognise the following items : – the codes of well-formed terms

– the names of variables occurrences within those terms 
– the types of values assigned to those occurrences  
– whether or not certain assignments occur only once per term 
– whether or not certain assignments have free variables 
– whether or not certain assignments are universally quantified 
– whether or not certain assignments existentially quantify 
– whether or not certain assignments are simply equations 
– whether or not certain assignments involve abstraction 
– whether or not certain assignments use tuples 
– whether or not certain assignments use arrays 
– whether or not certain assignments use records 
– whether or not certain assignments use functions 
– whether or not certain assignments use modules 
– whether or not certain assignments use classes 
– whether or not certain assignments use objects 
– whether or not certain assignments use interfaces 
– whether or not certain assignments use inheritance 
– whether or not certain assignments use polymorphism 
– whether or not certain assignments use recursion 
– whether or not certain assignments use loops 
– whether or not certain assignments use conditionals 
– whether or not certain assignments use guards 
– whether or not certain assignments use effects 
– whether or not certain assignments use side effects 
– whether or not certain assignments use mutualrecursion 
– whether or not certain assignments use coinduction 
– whether or not certain assignments use dependent function interpretation 
– whether or not certain assignments use dependent function extrapolation 
– whether or not certain assignments use dependent function elimination 
– whether or not certain assignments use dependent function inclusion 
– whether or not certain assignments use dependent function exclusion 
– whether or not certain assignments use dependent function application 
– whether or not certain assignments use dependent function composition 
– whether or not certain assignments use dependent function decomposition 
– whether or not certain assignments use dependent function factorization 
– whether or not certain assignments use dependent function generalization 
– whether or not certain assignments use dependent function specialization 
– whether or not certain assignments use dependent function inference 
– whether or not certain assignments use dependent function deduction 
– whether or not certain assignments use dependent function induction 
– whether or not certain assignments use dependent function coerc– the names of variables occurrences within those terms 
– the types of values assigned to those occurrences  
– whether or not certain assignments occur only once per term 
– whether or not certain assignments have free variables 
– whether or not certain assignments are universally quantified 
– whether or not certain assignments existentially quantify 
– whether or not certain assignments are simply equations 
– whether or not certain assignments involve abstraction 
– whether or not certain assignments use tuples 
– whether or not certain assignments use arrays 
– whether or not certain assignments use records 
– whether or not certain assignments use functions 
– whether or not certain assignments use modules 
– whether or not certain assignments use classes 
– whether or not certain assignments use objects 
– whether or not certain assignments use interfaces 
– whether or not certain assignments use inheritance 
– whether or not certain assignments use polymorphism 
– whether or not certain assignments use recursion 
– whether or not certain assignments use loops 
– whether or not certain assignments use conditionals 
– whether or not certain assignments use guards 
– whether or not certain assignments use effects 
– whether or not certain assignments use side effects 
– whether or not certain assignments use mutualrecursion 
– whether or not certain assignments use coinduction 
– whether or not certain assignments use dependent function interpretation 
– whether or not certain assignments use dependent function extrapolation 
– whether or not certain assignments use dependent function elimination 
– whether or not certain assignments use dependent function inclusion 
– whether or not certain assignments use dependent function exclusion 
– whether or not certain assignments use dependent function application 
– whether or not certain assignments use dependent function composition 
– whether or not certain assignments use dependent function decomposition 
– whether or not certain assignments use dependent function factorization 
– whether or not certain assignments use dependent function generalization 
– whether or not certain assignments use dependent function specialization 
– whether or not certain assignments use dependent function inference 
– whether or not certain assignments use dependent function deduction 
– whether or not certain assignments use dependent function induction 
– whether or not certain assignments use dependent function


You: !@>Seeker:#35 is equivalent to the syntactically similar definition written in Isabelle ’ s higher-order logic , which then is proved to satisfy deeper properties 
 The shadow predicates also give an easy way to refer to the truth of the corresponding HF predicate ; because each is defined to be a Σ formula , that gives a quick way ( using theorem Sigma fm imp thm above ) to show that some ground instance of the predicate can be proved formally in HF 
 Also , one way to arrive at the correct definition of an HF predicate is to define its shadow equivalent first , since proving that it implies the required properties is much easier in Isabelle/HOL ’ s native logic than in HF 
 Swierczkowski [ 32 ] defines a full set of syntactic predicate ´ s , leaving nothing as an exercise 
 Unfortunately , the introduction of de Bruijn syntax necessitates rewriting many of these definitions 
 Some predicates ( such as the variable occurrence test ) are replaced by others ( abstraction over a variable occurrence ) 
 The final list includes predicates to recognise the following items : – the codes of well-formed terms ( and constant terms , without variables ) – correct instances of abstraction ( of a term or formula ) over a variable – correct instances of substitution ( in a term or formula ) for a variable – the codes of well-formed formulas As explained below , abstraction over a formula needs to be defined before the notion of a formula itself 
 We also need the property of variable non-occurrence , “ x does not occur in A ” , which can be expressed directly as “ substituting 0 for x in A yields A ” 
 This little trick eliminates the need for a full definition 
 Each operation is first defined in its sequence form ( expressing that sequence s is built up in an appropriate way and that sk is a specific value ) ; existential quantification over s and k then yields the final predicate 
 Formalising the sequence of steps is a primitive way to express recursion 
 Moreover , it tends to yield Σ formulas 
 The simplest example is the predicate for constants 
 The shadow predicate can be defined with the help of BuildSeq , mentioned in Sect 
 3
2 above 
 Note that shadow predicates are written in ordinary higher-order logic , and refer to syntactic codes using set values 
 We see below that in the sequence buildup , each element is either 0 ( which is the code of the constant zero ) or else has the form q Eats v w , which is the code for v ⊳ w
 definition SeqConst : : `` hf ⇒ hf ⇒ hf ⇒ bool '' where `` SeqConst s k t ≡ BuildSeq ( λu 
 u=0 ) ( λu v w
 u = q Eats v w

Introspector: INPUT:!@>Seeker:#35 is equivalent to the syntactically similar definition written in Isabelle ’ s higher-order logic , which then is proved to satisfy deeper properties 
 The shadow predicates also give an easy way to refer to the truth of the corresponding HF predicate ; because each is defined to be a Σ formula , that gives a quick way ( using theorem Sigma fm imp thm above ) to show that some ground instance of the predicate can be proved formally in HF 
 Also , one way to arrive at the correct definition of an HF predicate is to define its shadow equivalent first , since proving that it implies the required properties is much easier in Isabelle/HOL ’ s native logic than in HF 
 Swierczkowski [ 32 ] defines a full set of syntactic predicate ´ s , leaving nothing as an exercise 
 Unfortunately , the introduction of de Bruijn syntax necessitates rewriting many of these definitions 
 Some predicates ( such as the variable occurrence test ) are replaced by others ( abstraction over a variable occurrence ) 
 The final list includes predicates to recognise the following items : – the codes of well-formed terms ( and constant terms , without variables ) – correct instances of abstraction ( of a term or formula ) over a variable – correct instances of substitution ( in a term or formula ) for a variable – the codes of well-formed formulas As explained below , abstraction over a formula needs to be defined before the notion of a formula itself 
 We also need the property of variable non-occurrence , “ x does not occur in A ” , which can be expressed directly as “ substituting 0 for x in A yields A ” 
 This little trick eliminates the need for a full definition 
 Each operation is first defined in its sequence form ( expressing that sequence s is built up in an appropriate way and that sk is a specific value ) ; existential quantification over s and k then yields the final predicate 
 Formalising the sequence of steps is a primitive way to express recursion 
 Moreover , it tends to yield Σ formulas 
 The simplest example is the predicate for constants 
 The shadow predicate can be defined with the help of BuildSeq , mentioned in Sect 
 3
2 above 
 Note that shadow predicates are written in ordinary higher-order logic , and refer to syntactic codes using set values 
 We see below that in the sequence buildup , each element is either 0 ( which is the code of the constant zero ) or else has the form q Eats v w , which is the code for v ⊳ w
 definition SeqConst : : `` hf ⇒ hf ⇒ hf ⇒ bool '' where `` SeqConst s k t ≡ BuildSeq ( λu 
 u=0 ) ( λu v w
 u = q Eats v w




































































































































































































































































































































































































































































































































You: !@>Seeker:#36 little trick eliminates the need for a full definition 
 Each operation is first defined in its sequence form ( expressing that sequence s is built up in an appropriate way and that sk is a specific value ) ; existential quantification over s and k then yields the final predicate 
 Formalising the sequence of steps is a primitive way to express recursion 
 Moreover , it tends to yield Σ formulas 
 The simplest example is the predicate for constants 
 The shadow predicate can be defined with the help of BuildSeq , mentioned in Sect 
 3
2 above 
 Note that shadow predicates are written in ordinary higher-order logic , and refer to syntactic codes using set values 
 We see below that in the sequence buildup , each element is either 0 ( which is the code of the constant zero ) or else has the form q Eats v w , which is the code for v ⊳ w
 definition SeqConst : : `` hf ⇒ hf ⇒ hf ⇒ bool '' where `` SeqConst s k t ≡ BuildSeq ( λu 
 u=0 ) ( λu v w
 u = q Eats v w ) s k t '' Thus a constant expression is built up from 0 using the ⊳ operator 
 The idea is that every element of the sequence is either 0 or has the form px ⊳ yq , where x and y occur earlier in the sequence 
 Most of the other syntactic predicates fit exactly the same pattern , but with different base cases and constructors 
 A function must be coded as a relation , and a typical base case might be h0 , 0i , other sequence elements having the form hpx ⊳ yq , px ′ ⊳ y ′ qi , where hx , x′ i and hy , y′ i occur earlier in the sequence 
 Substitution is codified in this manner 
 A function taking two arguments is coded as a sequence of triples , etc 
 The discussion above relates to shadow predicates , which define formulas of Isabelle/HOL relating HF sets 
 The real predicates , which denote formulas of the HF calculus , are based on exactly the same ideas except that the various set constructions must be expressed using the HF term language 
 Note that the real predicates typically have names ending with P
 18 The following formula again specifies the notion of a constant term 
 It is simply the result of expressing the definition of SeqConst using HF syntax , expanding the definition of BuildSeq 
 The syntactic sugar for a reference to a sequence element sm within some formula φ must now be expanded to its true form : φ ( sm ) becomes ∃y [ hm , yi ∈ s∧φ ( y ) ] 
 nominal primrec SeqConstP : : `` tm ⇒ tm ⇒ tm ⇒ fm '' where `` [ [ atom

Introspector: INPUT:!@>Seeker:#36 little trick eliminates the need for a full definition 
 Each operation is first defined in its sequence form ( expressing that sequence s is built up in an appropriate way and that sk is a specific value ) ; existential quantification over s and k then yields the final predicate 
 Formalising the sequence of steps is a primitive way to express recursion 
 Moreover , it tends to yield Σ formulas 
 The simplest example is the predicate for constants 
 The shadow predicate can be defined with the help of BuildSeq , mentioned in Sect 
 3
2 above 
 Note that shadow predicates are written in ordinary higher-order logic , and refer to syntactic codes using set values 
 We see below that in the sequence buildup , each element is either 0 ( which is the code of the constant zero ) or else has the form q Eats v w , which is the code for v ⊳ w
 definition SeqConst : : `` hf ⇒ hf ⇒ hf ⇒ bool '' where `` SeqConst s k t ≡ BuildSeq ( λu 
 u=0 ) ( λu v w
 u = q Eats v w ) s k t '' Thus a constant expression is built up from 0 using the ⊳ operator 
 The idea is that every element of the sequence is either 0 or has the form px ⊳ yq , where x and y occur earlier in the sequence 
 Most of the other syntactic predicates fit exactly the same pattern , but with different base cases and constructors 
 A function must be coded as a relation , and a typical base case might be h0 , 0i , other sequence elements having the form hpx ⊳ yq , px ′ ⊳ y ′ qi , where hx , x′ i and hy , y′ i occur earlier in the sequence 
 Substitution is codified in this manner 
 A function taking two arguments is coded as a sequence of triples , etc 
 The discussion above relates to shadow predicates , which define formulas of Isabelle/HOL relating HF sets 
 The real predicates , which denote formulas of the HF calculus , are based on exactly the same ideas except that the various set constructions must be expressed using the HF term language 
 Note that the real predicates typically have names ending with P
 18 The following formula again specifies the notion of a constant term 
 It is simply the result of expressing the definition of SeqConst using HF syntax , expanding the definition of BuildSeq 
 The syntactic sugar for a reference to a sequence element sm within some formula φ must now be expanded to its true form : φ ( sm ) becomes ∃y [ hm , yi ∈ s∧φ ( y ) ] 
 nominal primrec SeqConstP : : `` tm ⇒ tm ⇒ tm ⇒ fm '' where `` [ [ atom

nominal primrec BuildSeqP : : `atom ⇒ atom ⇒ atom ⇒ atom ' | atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atomnominal primrec BuildSeqP : : `atom ⇒ atom ⇒ atom ⇒ atom ' | atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧ atom ∧


You: !@>Seeker:#37 ′ ⊳ y ′ qi , where hx , x′ i and hy , y′ i occur earlier in the sequence 
 Substitution is codified in this manner 
 A function taking two arguments is coded as a sequence of triples , etc 
 The discussion above relates to shadow predicates , which define formulas of Isabelle/HOL relating HF sets 
 The real predicates , which denote formulas of the HF calculus , are based on exactly the same ideas except that the various set constructions must be expressed using the HF term language 
 Note that the real predicates typically have names ending with P
 18 The following formula again specifies the notion of a constant term 
 It is simply the result of expressing the definition of SeqConst using HF syntax , expanding the definition of BuildSeq 
 The syntactic sugar for a reference to a sequence element sm within some formula φ must now be expanded to its true form : φ ( sm ) becomes ∃y [ hm , yi ∈ s∧φ ( y ) ] 
 nominal primrec SeqConstP : : `` tm ⇒ tm ⇒ tm ⇒ fm '' where `` [ [ atom l ♯ ( s , k , sl , m , n , sm , sn ) ; atom sl ♯ ( s , m , n , sm , sn ) ; atom m ♯ ( s , n , sm , sn ) ; atom n ♯ ( s , sm , sn ) ; atom sm ♯ ( s , sn ) ; atom sn ♯ ( s ) ] ] =⇒ SeqConstP s k t = LstSeqP s k t AND All2 l ( SUCC k ) ( Ex sl ( HPair ( Var l ) ( Var sl ) IN s AND ( Var sl EQ Zero OR Ex m ( Ex n ( Ex sm ( Ex sn ( Var m IN Var l AND Var n IN Var l AND HPair ( Var m ) ( Var sm ) IN s AND HPair ( Var n ) ( Var sn ) IN s AND Var sl EQ Q Eats ( Var sm ) ( Var sn ) ) ) ) ) ) ) ) '' We have five bound variables , namely l , sl , m , sm , n , sn , which must be constrained to be distinct from one another using the freshness conditions shown 
 This nominal boilerplate may seem excessive 
 However , to define this predicate without nominal syntax , bound variable names might have to be calculated , perhaps by taking the maximum of the bound variables in s , k and t and continuing from there 
 Nominal constrains the variables more abstractly and flexibly 
 As mentioned above , sometimes we deal with sequences of pairs or triples , with correspondingly more complicated formulas 
 Where a predicate describes a function such as

Introspector: INPUT:!@>Seeker:#37 ′ ⊳ y ′ qi , where hx , x′ i and hy , y′ i occur earlier in the sequence 
 Substitution is codified in this manner 
 A function taking two arguments is coded as a sequence of triples , etc 
 The discussion above relates to shadow predicates , which define formulas of Isabelle/HOL relating HF sets 
 The real predicates , which denote formulas of the HF calculus , are based on exactly the same ideas except that the various set constructions must be expressed using the HF term language 
 Note that the real predicates typically have names ending with P
 18 The following formula again specifies the notion of a constant term 
 It is simply the result of expressing the definition of SeqConst using HF syntax , expanding the definition of BuildSeq 
 The syntactic sugar for a reference to a sequence element sm within some formula φ must now be expanded to its true form : φ ( sm ) becomes ∃y [ hm , yi ∈ s∧φ ( y ) ] 
 nominal primrec SeqConstP : : `` tm ⇒ tm ⇒ tm ⇒ fm '' where `` [ [ atom l ♯ ( s , k , sl , m , n , sm , sn ) ; atom sl ♯ ( s , m , n , sm , sn ) ; atom m ♯ ( s , n , sm , sn ) ; atom n ♯ ( s , sm , sn ) ; atom sm ♯ ( s , sn ) ; atom sn ♯ ( s ) ] ] =⇒ SeqConstP s k t = LstSeqP s k t AND All2 l ( SUCC k ) ( Ex sl ( HPair ( Var l ) ( Var sl ) IN s AND ( Var sl EQ Zero OR Ex m ( Ex n ( Ex sm ( Ex sn ( Var m IN Var l AND Var n IN Var l AND HPair ( Var m ) ( Var sm ) IN s AND HPair ( Var n ) ( Var sn ) IN s AND Var sl EQ Q Eats ( Var sm ) ( Var sn ) ) ) ) ) ) ) ) '' We have five bound variables , namely l , sl , m , sm , n , sn , which must be constrained to be distinct from one another using the freshness conditions shown 
 This nominal boilerplate may seem excessive 
 However , to define this predicate without nominal syntax , bound variable names might have to be calculated , perhaps by taking the maximum of the bound variables in s , k and t and continuing from there 
 Nominal constrains the variables more abstractly and flexibly 
 As mentioned above , sometimes we deal with sequences of pairs or triples , with correspondingly more complicated formulas 
 Where a predicate describes a function such as

```scss
  ```

























































































































































































































































































































































































































































































































```scss
  ```


You: !@>Seeker:#38 ( Var sl ) IN s AND ( Var sl EQ Zero OR Ex m ( Ex n ( Ex sm ( Ex sn ( Var m IN Var l AND Var n IN Var l AND HPair ( Var m ) ( Var sm ) IN s AND HPair ( Var n ) ( Var sn ) IN s AND Var sl EQ Q Eats ( Var sm ) ( Var sn ) ) ) ) ) ) ) ) '' We have five bound variables , namely l , sl , m , sm , n , sn , which must be constrained to be distinct from one another using the freshness conditions shown 
 This nominal boilerplate may seem excessive 
 However , to define this predicate without nominal syntax , bound variable names might have to be calculated , perhaps by taking the maximum of the bound variables in s , k and t and continuing from there 
 Nominal constrains the variables more abstractly and flexibly 
 As mentioned above , sometimes we deal with sequences of pairs or triples , with correspondingly more complicated formulas 
 Where a predicate describes a function such as substitution , the sequence being built up consists of ordered pairs of arguments and results , and there are typically nine bound variables 
 To perform abstraction over a formula requires keeping track of the depth of quantifier nesting during recursion 
 This is a two-argument function , so the sequence being built up consists of ordered triples and there are 12 bound variables 
 Although the nominal system copes with these complicated expressions , the processing time can be measured in tens of seconds 
 Now that we have defined the buildup of a sequence of constants , a constant itself is trivial 
 The existence of any properly formed sequence s of length k culminating with some term t guarantees that t is a constant term 
 Here are both the shadow and HF calculus versions of the predicate 
 definition Const : : `` hf ⇒ bool '' where `` Const t ≡ ( ∃ s k
 SeqConst s k t ) '' nominal primrec ConstP : : `` tm ⇒ fm '' where `` [ [ atom k ♯ ( s , t ) ; atom s ♯ t ] ] =⇒ ConstP t = Ex s ( Ex k ( SeqConstP ( Var s ) ( Var k ) t ) ) '' Why don ’ t we define the HF predicate BuildSeqP analogously to BuildSeq , which expresses the definition of SeqConst so succinctly ? Then we might expect to avoid the mess above , defining a predicate such as SeqConstP in a single line 
 This was actually attempted , but the nominal system is not really suitable for formalising higher-order definitions 
 Complicated auxiliary definitions and proofs are required 
 It is easier simply to write out the definitions , especially as

Introspector: INPUT:!@>Seeker:#38 ( Var sl ) IN s AND ( Var sl EQ Zero OR Ex m ( Ex n ( Ex sm ( Ex sn ( Var m IN Var l AND Var n IN Var l AND HPair ( Var m ) ( Var sm ) IN s AND HPair ( Var n ) ( Var sn ) IN s AND Var sl EQ Q Eats ( Var sm ) ( Var sn ) ) ) ) ) ) ) ) '' We have five bound variables , namely l , sl , m , sm , n , sn , which must be constrained to be distinct from one another using the freshness conditions shown 
 This nominal boilerplate may seem excessive 
 However , to define this predicate without nominal syntax , bound variable names might have to be calculated , perhaps by taking the maximum of the bound variables in s , k and t and continuing from there 
 Nominal constrains the variables more abstractly and flexibly 
 As mentioned above , sometimes we deal with sequences of pairs or triples , with correspondingly more complicated formulas 
 Where a predicate describes a function such as substitution , the sequence being built up consists of ordered pairs of arguments and results , and there are typically nine bound variables 
 To perform abstraction over a formula requires keeping track of the depth of quantifier nesting during recursion 
 This is a two-argument function , so the sequence being built up consists of ordered triples and there are 12 bound variables 
 Although the nominal system copes with these complicated expressions , the processing time can be measured in tens of seconds 
 Now that we have defined the buildup of a sequence of constants , a constant itself is trivial 
 The existence of any properly formed sequence s of length k culminating with some term t guarantees that t is a constant term 
 Here are both the shadow and HF calculus versions of the predicate 
 definition Const : : `` hf ⇒ bool '' where `` Const t ≡ ( ∃ s k
 SeqConst s k t ) '' nominal primrec ConstP : : `` tm ⇒ fm '' where `` [ [ atom k ♯ ( s , t ) ; atom s ♯ t ] ] =⇒ ConstP t = Ex s ( Ex k ( SeqConstP ( Var s ) ( Var k ) t ) ) '' Why don ’ t we define the HF predicate BuildSeqP analogously to BuildSeq , which expresses the definition of SeqConst so succinctly ? Then we might expect to avoid the mess above , defining a predicate such as SeqConstP in a single line 
 This was actually attempted , but the nominal system is not really suitable for formalising higher-order definitions 
 Complicated auxiliary definitions and proofs are required 
 It is easier simply to write out the definitions , especially as

the number of bindings increases .”</s>the number of bindings increases


You: !@>Seeker:#39 constant itself is trivial 
 The existence of any properly formed sequence s of length k culminating with some term t guarantees that t is a constant term 
 Here are both the shadow and HF calculus versions of the predicate 
 definition Const : : `` hf ⇒ bool '' where `` Const t ≡ ( ∃ s k
 SeqConst s k t ) '' nominal primrec ConstP : : `` tm ⇒ fm '' where `` [ [ atom k ♯ ( s , t ) ; atom s ♯ t ] ] =⇒ ConstP t = Ex s ( Ex k ( SeqConstP ( Var s ) ( Var k ) t ) ) '' Why don ’ t we define the HF predicate BuildSeqP analogously to BuildSeq , which expresses the definition of SeqConst so succinctly ? Then we might expect to avoid the mess above , defining a predicate such as SeqConstP in a single line 
 This was actually attempted , but the nominal system is not really suitable for formalising higher-order definitions 
 Complicated auxiliary definitions and proofs are required 
 It is easier simply to write out the definitions , especially as their very repetitiveness allows proof development by cut and paste 
 One tiny consolidation has been done 
 We need to define the predicates Term and TermP analogously to Const and ConstP above but allowing variables 
 The question of whether variables are allowed in a term or not can be governed by a Boolean 
 The proof development therefore introduces the predicate SeqCTermP , taking a Boolean argument , from which SeqTermP and SeqConstP are trivially obtained 
 19 abbreviation SeqTermP : : `` tm ⇒ tm ⇒ tm ⇒ fm '' where `` SeqTermP ≡ SeqCTermP True '' abbreviation SeqConstP : : `` tm ⇒ tm ⇒ tm ⇒ fm '' where `` SeqConstP ≡ SeqCTermP False '' In this way , we can define the very similar predicates TermP and ConstP with a minimum of repeated material 
 Many other predicates must be defined 
 Abstraction and substitution must be defined separately for terms , atomic formulas and formulas 
 Here are the shadow definitions of abstraction and substitution for terms 
 They are similar enough ( both involve replacing a variable ) that a single function , SeqStTerm , can express both 
 BuildSeq2 is similar to BuildSeq above , but constructs a sequence of pairs 
 definition SeqStTerm : : `` hf ⇒ hf ⇒ hf ⇒ hf ⇒ hf ⇒ hf ⇒ bool '' where `` SeqStTerm v u x x ’ s k ≡ is Var v ∧ BuildSeq2 ( λy y ’ 
 ( is Ind y ∨ Ord y ) ∧ y ’ = ( if y=v then u else y ) ) ( λu u ’ v v ’ w w ’ 
 u = q Eats v w ∧ u ’ = q Eats v ’ w ’ )

Introspector: INPUT:!@>Seeker:#39 constant itself is trivial 
 The existence of any properly formed sequence s of length k culminating with some term t guarantees that t is a constant term 
 Here are both the shadow and HF calculus versions of the predicate 
 definition Const : : `` hf ⇒ bool '' where `` Const t ≡ ( ∃ s k
 SeqConst s k t ) '' nominal primrec ConstP : : `` tm ⇒ fm '' where `` [ [ atom k ♯ ( s , t ) ; atom s ♯ t ] ] =⇒ ConstP t = Ex s ( Ex k ( SeqConstP ( Var s ) ( Var k ) t ) ) '' Why don ’ t we define the HF predicate BuildSeqP analogously to BuildSeq , which expresses the definition of SeqConst so succinctly ? Then we might expect to avoid the mess above , defining a predicate such as SeqConstP in a single line 
 This was actually attempted , but the nominal system is not really suitable for formalising higher-order definitions 
 Complicated auxiliary definitions and proofs are required 
 It is easier simply to write out the definitions , especially as their very repetitiveness allows proof development by cut and paste 
 One tiny consolidation has been done 
 We need to define the predicates Term and TermP analogously to Const and ConstP above but allowing variables 
 The question of whether variables are allowed in a term or not can be governed by a Boolean 
 The proof development therefore introduces the predicate SeqCTermP , taking a Boolean argument , from which SeqTermP and SeqConstP are trivially obtained 
 19 abbreviation SeqTermP : : `` tm ⇒ tm ⇒ tm ⇒ fm '' where `` SeqTermP ≡ SeqCTermP True '' abbreviation SeqConstP : : `` tm ⇒ tm ⇒ tm ⇒ fm '' where `` SeqConstP ≡ SeqCTermP False '' In this way , we can define the very similar predicates TermP and ConstP with a minimum of repeated material 
 Many other predicates must be defined 
 Abstraction and substitution must be defined separately for terms , atomic formulas and formulas 
 Here are the shadow definitions of abstraction and substitution for terms 
 They are similar enough ( both involve replacing a variable ) that a single function , SeqStTerm , can express both 
 BuildSeq2 is similar to BuildSeq above , but constructs a sequence of pairs 
 definition SeqStTerm : : `` hf ⇒ hf ⇒ hf ⇒ hf ⇒ hf ⇒ hf ⇒ bool '' where `` SeqStTerm v u x x ’ s k ≡ is Var v ∧ BuildSeq2 ( λy y ’ 
 ( is Ind y ∨ Ord y ) ∧ y ’ = ( if y=v then u else y ) ) ( λu u ’ v v ’ w w ’ 
 u = q Eats v w ∧ u ’ = q Eats v ’ w ’ )

The first step in understanding these lines is recognizing them as an attempt at describing the process of building up mathematical expressions through a series of small steps, each consisting of a pair of subexpressions connected by a logical operator. These steps are meant to resemble the structure of a traditional programming language's control flow statements, like `if`/`else`. However, unlike those statements, they do not have a direct equivalent in standard mathematics; instead, they represent a novel approach to organizing complex reasoning tasks within a formal system.
Now let us dive deeper into what these lines aim to convey!
In the first line `@>`Seeker:#39`, we encounter a reference to a numbered section (`#39`). This indicates that there follows a specific passage related to the topic being discussed earlier in the document. By conventionally assigning numbers to sections within documents, authors create navigable structures enabling readers quickly locate relevant content without having to search endlessly through dense text passages. So here `#39` likely corresponds to one particular point made about constants somewhere along the article’s course – perhaps something regarding how certain values hold significance across different contexts? As our wise old mentor continues guiding us further down this esoteric pathway...</s>The first step in understanding these lines is recognizing them as an attempt at describing the process of building up mathematical expressions through a series of small steps, each consisting of a pair of subexpressions connected by a logical operator. These steps are meant to resemble the structure of a traditional programming language's control flow statements, like `if`/`else`. However, unlike those statements, they do not have a direct equivalent in standard mathematics; instead, they represent a novel approach to organizing complex reasoning tasks within a formal system.
Now let us dive deeper into what these lines aim to convey!
In the first line `@>`Seeker:#39`, we encounter a reference to a numbered section (`#39`). This indicates that there follows a specific passage related to the topic being discussed earlier in the document. By conventionally assigning numbers to sections within documents, authors create navigable structures enabling readers quickly locate relevant content without having to search endlessly through dense text passages. So here `#39` likely corresponds to one particular point made about constants somewhere along the article’s course – perhaps something regarding how certain values hold significance across different contexts? As our wise old mentor continues guiding us further down this esoteric


You: !@>Seeker:#40 abbreviation SeqConstP : : `` tm ⇒ tm ⇒ tm ⇒ fm '' where `` SeqConstP ≡ SeqCTermP False '' In this way , we can define the very similar predicates TermP and ConstP with a minimum of repeated material 
 Many other predicates must be defined 
 Abstraction and substitution must be defined separately for terms , atomic formulas and formulas 
 Here are the shadow definitions of abstraction and substitution for terms 
 They are similar enough ( both involve replacing a variable ) that a single function , SeqStTerm , can express both 
 BuildSeq2 is similar to BuildSeq above , but constructs a sequence of pairs 
 definition SeqStTerm : : `` hf ⇒ hf ⇒ hf ⇒ hf ⇒ hf ⇒ hf ⇒ bool '' where `` SeqStTerm v u x x ’ s k ≡ is Var v ∧ BuildSeq2 ( λy y ’ 
 ( is Ind y ∨ Ord y ) ∧ y ’ = ( if y=v then u else y ) ) ( λu u ’ v v ’ w w ’ 
 u = q Eats v w ∧ u ’ = q Eats v ’ w ’ ) s k x x ’ '' definition AbstTerm : : `` hf ⇒ hf ⇒ hf ⇒ hf ⇒ bool '' where `` AbstTerm v i x x ’ ≡ Ord i ∧ ( ∃ s k
 SeqStTerm v ( q Ind i ) x x ’ s k ) '' definition SubstTerm : : `` hf ⇒ hf ⇒ hf ⇒ hf ⇒ bool '' where `` SubstTerm v u x x ’ ≡ Term u ∧ ( ∃ s k
 SeqStTerm v u x x ’ s k ) '' Abstraction over formulas ( AbstForm/AbstFormP ) must be defined before formulas themselves , in order to formalise existential quantification 
 There is no circularity here : the abstraction operation can be defined independently of the notion of a well-formed formula , and is not restricted to them 
 The definition involves sequences of triples and is too complicated to present here 
 With abstraction over formulas defined , we can finally define the concept of a formula itself 
 An Atomic formula involves two terms , combined using the relations EQ or IN 
 Then MakeForm combines one or two existing formulas to build more complex ones 
 It constrains y to be the code of a formula constructed from existing formulas u and v by the disjunction u ∨ v , the negation ¬u or the existential formula ∃ ( u ’ ) , where u ’ has been obtained by abstracting u over some variable , v via the predicate AbstForm 
 definition MakeForm : : `` hf ⇒ hf ⇒ hf ⇒ bool '' where `` MakeForm y u w ≡ y = q Disj u w ∨ y = q Neg u ∨ ( ∃ v u ’ 
 AbstForm v 0 u u

Introspector: INPUT:!@>Seeker:#40 abbreviation SeqConstP : : `` tm ⇒ tm ⇒ tm ⇒ fm '' where `` SeqConstP ≡ SeqCTermP False '' In this way , we can define the very similar predicates TermP and ConstP with a minimum of repeated material 
 Many other predicates must be defined 
 Abstraction and substitution must be defined separately for terms , atomic formulas and formulas 
 Here are the shadow definitions of abstraction and substitution for terms 
 They are similar enough ( both involve replacing a variable ) that a single function , SeqStTerm , can express both 
 BuildSeq2 is similar to BuildSeq above , but constructs a sequence of pairs 
 definition SeqStTerm : : `` hf ⇒ hf ⇒ hf ⇒ hf ⇒ hf ⇒ hf ⇒ bool '' where `` SeqStTerm v u x x ’ s k ≡ is Var v ∧ BuildSeq2 ( λy y ’ 
 ( is Ind y ∨ Ord y ) ∧ y ’ = ( if y=v then u else y ) ) ( λu u ’ v v ’ w w ’ 
 u = q Eats v w ∧ u ’ = q Eats v ’ w ’ ) s k x x ’ '' definition AbstTerm : : `` hf ⇒ hf ⇒ hf ⇒ hf ⇒ bool '' where `` AbstTerm v i x x ’ ≡ Ord i ∧ ( ∃ s k
 SeqStTerm v ( q Ind i ) x x ’ s k ) '' definition SubstTerm : : `` hf ⇒ hf ⇒ hf ⇒ hf ⇒ bool '' where `` SubstTerm v u x x ’ ≡ Term u ∧ ( ∃ s k
 SeqStTerm v u x x ’ s k ) '' Abstraction over formulas ( AbstForm/AbstFormP ) must be defined before formulas themselves , in order to formalise existential quantification 
 There is no circularity here : the abstraction operation can be defined independently of the notion of a well-formed formula , and is not restricted to them 
 The definition involves sequences of triples and is too complicated to present here 
 With abstraction over formulas defined , we can finally define the concept of a formula itself 
 An Atomic formula involves two terms , combined using the relations EQ or IN 
 Then MakeForm combines one or two existing formulas to build more complex ones 
 It constrains y to be the code of a formula constructed from existing formulas u and v by the disjunction u ∨ v , the negation ¬u or the existential formula ∃ ( u ’ ) , where u ’ has been obtained by abstracting u over some variable , v via the predicate AbstForm 
 definition MakeForm : : `` hf ⇒ hf ⇒ hf ⇒ bool '' where `` MakeForm y u w ≡ y = q Disj u w ∨ y = q Neg u ∨ ( ∃ v u ’ 
 AbstForm v 0 u u

y = q Exist v 0 u u '’ w )''
The rest of the program consists mainly of defining various functions which take these basic building blocks as arguments and return new instances thereof . These include things like `BuildSeq` which builds an infinite sequence of pairs given another pair , `MakeAtom` which takes an atom and returns its corresponding term , etcetera .</s>y = q Exist v 0 u u '’ w )''
The rest of the program consists mainly of defining various functions which take these basic building blocks as arguments and return new instances thereof . These include things like `BuildSeq` which builds an infinite sequence of pairs given another pair , `MakeAtom` which takes an atom and returns its corresponding term , etcetera


You: !@>Seeker:#41 defined before formulas themselves , in order to formalise existential quantification 
 There is no circularity here : the abstraction operation can be defined independently of the notion of a well-formed formula , and is not restricted to them 
 The definition involves sequences of triples and is too complicated to present here 
 With abstraction over formulas defined , we can finally define the concept of a formula itself 
 An Atomic formula involves two terms , combined using the relations EQ or IN 
 Then MakeForm combines one or two existing formulas to build more complex ones 
 It constrains y to be the code of a formula constructed from existing formulas u and v by the disjunction u ∨ v , the negation ¬u or the existential formula ∃ ( u ’ ) , where u ’ has been obtained by abstracting u over some variable , v via the predicate AbstForm 
 definition MakeForm : : `` hf ⇒ hf ⇒ hf ⇒ bool '' where `` MakeForm y u w ≡ y = q Disj u w ∨ y = q Neg u ∨ ( ∃ v u ’ 
 AbstForm v 0 u u ’ ∧ y = q Ex u ’ ) '' nominal primrec MakeFormP : : `` tm ⇒ tm ⇒ tm ⇒ fm '' where `` [ [ atom v ♯ ( y , u , w , au ) ; atom au ♯ ( y , u , w ) ] ] =⇒ MakeFormP y u w = y EQ Q Disj u w OR y EQ Q Neg u OR Ex v ( Ex au ( AbstFormP ( Var v ) Zero u ( Var au ) AND y EQ Q Ex ( Var au ) ) ) '' Now , the sequence buildup of a formula can be defined with Atomic covering the base case and MakeForm expressing one level of the construction 
 Using similar methods to those illustrated above for constant terms , we arrive at the shadow predicate Form and the corresponding HF predicate FormP 
 4
3 Verifying the Coding Predicates Most textbook presentations take the correctness of such definitions as obvious , and indeed many properties are not difficult to prove 
 To show that the predicate Term 20 accepts all coded terms , a necessary lemma is to show the analogous property for well-formed de Bruijn terms : lemma wf Term quot dbtm : assumes `` wf dbtm u '' shows `` Term [ [ quot dbtm u ] ] e '' The proof is by induction on the construction of u ( in other words , on the inductive definition of wf dbtm u ) , and is routine by the definitions of the predicates Term and SeqTerm 
 This implies the desired result for terms , by the ( overloaded ) definition of ⌈t⌉ 
 corollary Term quot tm : fixes t : :tm shows `` Term [ [ ⌈t⌉

Introspector: INPUT:!@>Seeker:#41 defined before formulas themselves , in order to formalise existential quantification 
 There is no circularity here : the abstraction operation can be defined independently of the notion of a well-formed formula , and is not restricted to them 
 The definition involves sequences of triples and is too complicated to present here 
 With abstraction over formulas defined , we can finally define the concept of a formula itself 
 An Atomic formula involves two terms , combined using the relations EQ or IN 
 Then MakeForm combines one or two existing formulas to build more complex ones 
 It constrains y to be the code of a formula constructed from existing formulas u and v by the disjunction u ∨ v , the negation ¬u or the existential formula ∃ ( u ’ ) , where u ’ has been obtained by abstracting u over some variable , v via the predicate AbstForm 
 definition MakeForm : : `` hf ⇒ hf ⇒ hf ⇒ bool '' where `` MakeForm y u w ≡ y = q Disj u w ∨ y = q Neg u ∨ ( ∃ v u ’ 
 AbstForm v 0 u u ’ ∧ y = q Ex u ’ ) '' nominal primrec MakeFormP : : `` tm ⇒ tm ⇒ tm ⇒ fm '' where `` [ [ atom v ♯ ( y , u , w , au ) ; atom au ♯ ( y , u , w ) ] ] =⇒ MakeFormP y u w = y EQ Q Disj u w OR y EQ Q Neg u OR Ex v ( Ex au ( AbstFormP ( Var v ) Zero u ( Var au ) AND y EQ Q Ex ( Var au ) ) ) '' Now , the sequence buildup of a formula can be defined with Atomic covering the base case and MakeForm expressing one level of the construction 
 Using similar methods to those illustrated above for constant terms , we arrive at the shadow predicate Form and the corresponding HF predicate FormP 
 4
3 Verifying the Coding Predicates Most textbook presentations take the correctness of such definitions as obvious , and indeed many properties are not difficult to prove 
 To show that the predicate Term 20 accepts all coded terms , a necessary lemma is to show the analogous property for well-formed de Bruijn terms : lemma wf Term quot dbtm : assumes `` wf dbtm u '' shows `` Term [ [ quot dbtm u ] ] e '' The proof is by induction on the construction of u ( in other words , on the inductive definition of wf dbtm u ) , and is routine by the definitions of the predicates Term and SeqTerm 
 This implies the desired result for terms , by the ( overloaded ) definition of ⌈t⌉ 
 corollary Term quot tm : fixes t : :tm shows `` Term [ [ ⌈t⌉

The main idea behind these lemmas is to use the fact that any term can be expressed as an atomic formula involving only variables and constants . By showing that each step of the construction process preserves the required properties under certain conditions , it follows immediately that the final formula will satisfy the desired constraints 
In particular , the first part of the second lemma uses the fact that if a term contains a subterm U then there must be a variable occurring free in U which corresponds to a variable in the outermost context 

In summary , the key insight underlying these results is that the syntax of programming languages provides a rich source of structured data structures whose manipulation can be guided by mathematical techniques drawn from category theory </s>The main idea behind these lemmas is to use the fact that any term can be expressed as an atomic formula involving only variables and constants . By showing that each step of the construction process preserves the required properties under certain conditions , it follows immediately that the final formula will satisfy the desired constraints 
In particular , the first part of the second lemma uses the fact that if a term contains a subterm U then there must be a variable occurring free in U which corresponds to a variable in the outermost context 

In summary , the key insight underlying these results is that the syntax of programming languages provides a rich source of structured data structures whose manipulation can be guided by mathematical techniques drawn from category theory


You: !@>Seeker:#42 '' Now , the sequence buildup of a formula can be defined with Atomic covering the base case and MakeForm expressing one level of the construction 
 Using similar methods to those illustrated above for constant terms , we arrive at the shadow predicate Form and the corresponding HF predicate FormP 
 4
3 Verifying the Coding Predicates Most textbook presentations take the correctness of such definitions as obvious , and indeed many properties are not difficult to prove 
 To show that the predicate Term 20 accepts all coded terms , a necessary lemma is to show the analogous property for well-formed de Bruijn terms : lemma wf Term quot dbtm : assumes `` wf dbtm u '' shows `` Term [ [ quot dbtm u ] ] e '' The proof is by induction on the construction of u ( in other words , on the inductive definition of wf dbtm u ) , and is routine by the definitions of the predicates Term and SeqTerm 
 This implies the desired result for terms , by the ( overloaded ) definition of ⌈t⌉ 
 corollary Term quot tm : fixes t : :tm shows `` Term [ [ ⌈t⌉ ] ] e '' Note that both results concern the shadow predicate Term , not the HF predicate TermP 
 The argument of Term is a set , denoted using the evaluation operator , [ [ 


 ] ] e
 Direct proofs about HF predicates are long and tiresome 
 Fortunately , many such questions can be reduced to the corresponding questions involving shadow predicates , because codes are ground terms ; then the theorem Sigma fm imp thm guarantees the existence of a proof , sparing us the need to construct one 
 The converse correctness property must also be proved , namely that everything accepted by Term actually is the code of some term 
 The proof requires a lemma about the predicate SeqTerm 
 The reasoning is simply that constants and variables are wellformed , and that combining two well-formed terms preserves this property 
 Such proofs are streamlined through the use of BuildSeq induct , a derived rule for reasoning about sequence construction by induction on the length of the sequence 
 lemma Term imp wf dbtm : assumes `` Term x '' obtains t : :dbtm where `` wf dbtm t '' `` x = [ [ quot dbtm t ] ] e '' By the meaning of obtains , we see that if Term x then there exists some well-formed de Bruijn term t whose code evaluates to x 
 Since for every well-formed de Bruijn term there exists an equivalent standard term of type tm , we can conclude that Term x implies that x is the code of some term 
 corollary Term imp is tm : assumes `` Term x '' obtains t : :tm where `` x = [ [ ⌈t⌉ ] ] e '' Similar theorems—with similar proofs—are necessary

Introspector: INPUT:!@>Seeker:#42 '' Now , the sequence buildup of a formula can be defined with Atomic covering the base case and MakeForm expressing one level of the construction 
 Using similar methods to those illustrated above for constant terms , we arrive at the shadow predicate Form and the corresponding HF predicate FormP 
 4
3 Verifying the Coding Predicates Most textbook presentations take the correctness of such definitions as obvious , and indeed many properties are not difficult to prove 
 To show that the predicate Term 20 accepts all coded terms , a necessary lemma is to show the analogous property for well-formed de Bruijn terms : lemma wf Term quot dbtm : assumes `` wf dbtm u '' shows `` Term [ [ quot dbtm u ] ] e '' The proof is by induction on the construction of u ( in other words , on the inductive definition of wf dbtm u ) , and is routine by the definitions of the predicates Term and SeqTerm 
 This implies the desired result for terms , by the ( overloaded ) definition of ⌈t⌉ 
 corollary Term quot tm : fixes t : :tm shows `` Term [ [ ⌈t⌉ ] ] e '' Note that both results concern the shadow predicate Term , not the HF predicate TermP 
 The argument of Term is a set , denoted using the evaluation operator , [ [ 


 ] ] e
 Direct proofs about HF predicates are long and tiresome 
 Fortunately , many such questions can be reduced to the corresponding questions involving shadow predicates , because codes are ground terms ; then the theorem Sigma fm imp thm guarantees the existence of a proof , sparing us the need to construct one 
 The converse correctness property must also be proved , namely that everything accepted by Term actually is the code of some term 
 The proof requires a lemma about the predicate SeqTerm 
 The reasoning is simply that constants and variables are wellformed , and that combining two well-formed terms preserves this property 
 Such proofs are streamlined through the use of BuildSeq induct , a derived rule for reasoning about sequence construction by induction on the length of the sequence 
 lemma Term imp wf dbtm : assumes `` Term x '' obtains t : :dbtm where `` wf dbtm t '' `` x = [ [ quot dbtm t ] ] e '' By the meaning of obtains , we see that if Term x then there exists some well-formed de Bruijn term t whose code evaluates to x 
 Since for every well-formed de Bruijn term there exists an equivalent standard term of type tm , we can conclude that Term x implies that x is the code of some term 
 corollary Term imp is tm : assumes `` Term x '' obtains t : :tm where `` x = [ [ ⌈t⌉ ] ] e '' Similar theorems—with similar proofs—are necessary




































































































































































































































































































































































































































































































































You: !@>Seeker:#43 be proved , namely that everything accepted by Term actually is the code of some term 
 The proof requires a lemma about the predicate SeqTerm 
 The reasoning is simply that constants and variables are wellformed , and that combining two well-formed terms preserves this property 
 Such proofs are streamlined through the use of BuildSeq induct , a derived rule for reasoning about sequence construction by induction on the length of the sequence 
 lemma Term imp wf dbtm : assumes `` Term x '' obtains t : :dbtm where `` wf dbtm t '' `` x = [ [ quot dbtm t ] ] e '' By the meaning of obtains , we see that if Term x then there exists some well-formed de Bruijn term t whose code evaluates to x 
 Since for every well-formed de Bruijn term there exists an equivalent standard term of type tm , we can conclude that Term x implies that x is the code of some term 
 corollary Term imp is tm : assumes `` Term x '' obtains t : :tm where `` x = [ [ ⌈t⌉ ] ] e '' Similar theorems—with similar proofs—are necessary for each of the syntactic predicates 
 For example , the following result expresses that SubstForm correctly models the result A ( i : :=t ) of substituting t for i in the formula A
 lemma SubstForm quot unique : '' SubstForm ( q Var i ) [ [ ⌈t⌉ ] ] e [ [ ⌈A⌉ ] ] e x ’ ←→ x ’ = [ [ ⌈A ( i : :=t ) ⌉ ] ] e '' 4
4 Predicates for the Coding of Deduction On the whole , the formalisation of deduction is quite different from the formalisation of syntactic operations , which mostly involve simulated recursion over terms or formulas 
 A proof step in the HF calculus is an axiom , an axiom scheme or an inference rule 
 Axioms and propositional inference rules are straightforward to recognise using the existing syntactic primitives 
 Simply x EQ ⌈refl ax⌉ tests whether x denotes the reflexivity axiom 
 More complicated are inference rules involving quantification , where several syntactic conditions including abstraction and substitution need to be checked in sequence 
 For example , consider specialisation axioms of the form φ ( t/x ) → ∃x φ 
 21 nominal primrec Special axP : : `` tm ⇒ fm '' where '' [ [ atom v ♯ ( p , sx , y , ax , x ) ; atom x ♯ ( p , sx , y , ax ) ; atom ax ♯ ( p , sx , y ) ; atom y ♯ ( p , sx ) ; atom sx ♯ p ] ] =⇒ Special axP p = Ex v ( Ex x ( Ex ax ( Ex y ( Ex sx ( FormP ( Var x ) AND VarP ( Var v

Introspector: INPUT:!@>Seeker:#43 be proved , namely that everything accepted by Term actually is the code of some term 
 The proof requires a lemma about the predicate SeqTerm 
 The reasoning is simply that constants and variables are wellformed , and that combining two well-formed terms preserves this property 
 Such proofs are streamlined through the use of BuildSeq induct , a derived rule for reasoning about sequence construction by induction on the length of the sequence 
 lemma Term imp wf dbtm : assumes `` Term x '' obtains t : :dbtm where `` wf dbtm t '' `` x = [ [ quot dbtm t ] ] e '' By the meaning of obtains , we see that if Term x then there exists some well-formed de Bruijn term t whose code evaluates to x 
 Since for every well-formed de Bruijn term there exists an equivalent standard term of type tm , we can conclude that Term x implies that x is the code of some term 
 corollary Term imp is tm : assumes `` Term x '' obtains t : :tm where `` x = [ [ ⌈t⌉ ] ] e '' Similar theorems—with similar proofs—are necessary for each of the syntactic predicates 
 For example , the following result expresses that SubstForm correctly models the result A ( i : :=t ) of substituting t for i in the formula A
 lemma SubstForm quot unique : '' SubstForm ( q Var i ) [ [ ⌈t⌉ ] ] e [ [ ⌈A⌉ ] ] e x ’ ←→ x ’ = [ [ ⌈A ( i : :=t ) ⌉ ] ] e '' 4
4 Predicates for the Coding of Deduction On the whole , the formalisation of deduction is quite different from the formalisation of syntactic operations , which mostly involve simulated recursion over terms or formulas 
 A proof step in the HF calculus is an axiom , an axiom scheme or an inference rule 
 Axioms and propositional inference rules are straightforward to recognise using the existing syntactic primitives 
 Simply x EQ ⌈refl ax⌉ tests whether x denotes the reflexivity axiom 
 More complicated are inference rules involving quantification , where several syntactic conditions including abstraction and substitution need to be checked in sequence 
 For example , consider specialisation axioms of the form φ ( t/x ) → ∃x φ 
 21 nominal primrec Special axP : : `` tm ⇒ fm '' where '' [ [ atom v ♯ ( p , sx , y , ax , x ) ; atom x ♯ ( p , sx , y , ax ) ; atom ax ♯ ( p , sx , y ) ; atom y ♯ ( p , sx ) ; atom sx ♯ p ] ] =⇒ Special axP p = Ex v ( Ex x ( Ex ax ( Ex y ( Ex sx ( FormP ( Var x ) AND VarP ( Var v

Inference rules such as these require careful attention to detail when checking their validity .”</s>Inference rules such as these require careful attention to detail when checking their validity


You: !@>Seeker:#44 syntactic operations , which mostly involve simulated recursion over terms or formulas 
 A proof step in the HF calculus is an axiom , an axiom scheme or an inference rule 
 Axioms and propositional inference rules are straightforward to recognise using the existing syntactic primitives 
 Simply x EQ ⌈refl ax⌉ tests whether x denotes the reflexivity axiom 
 More complicated are inference rules involving quantification , where several syntactic conditions including abstraction and substitution need to be checked in sequence 
 For example , consider specialisation axioms of the form φ ( t/x ) → ∃x φ 
 21 nominal primrec Special axP : : `` tm ⇒ fm '' where '' [ [ atom v ♯ ( p , sx , y , ax , x ) ; atom x ♯ ( p , sx , y , ax ) ; atom ax ♯ ( p , sx , y ) ; atom y ♯ ( p , sx ) ; atom sx ♯ p ] ] =⇒ Special axP p = Ex v ( Ex x ( Ex ax ( Ex y ( Ex sx ( FormP ( Var x ) AND VarP ( Var v ) AND TermP ( Var y ) AND AbstFormP ( Var v ) Zero ( Var x ) ( Var ax ) AND SubstFormP ( Var v ) ( Var y ) ( Var x ) ( Var sx ) AND p EQ Q Imp ( Var sx ) ( Q Ex ( Var ax ) ) ) ) ) ) ) '' This definition states that a specialisation axiom is created from a formula x , a variable v and a term y , combined by appropriate abstraction and substitution operations 
 Correctness means proving that this predicate exactly characterises the elements of the set special axioms , which was used to define the HF calculus 
 The most complicated such scheme is the induction axiom HF3 ( defined in Sect 
 2
2 ) , with its three quantifiers 
 The treatment of the induction axiom requires nearly 180 lines , of which 120 are devoted to proving correctness with respect to the HF calculus 
 A proof of a theorem y is a sequence s of axioms and inference rules , ending with y : definition Prf : : `` hf ⇒ hf ⇒ hf ⇒ bool '' where `` Prf s k y ≡ BuildSeq ( λx 
 x ∈ Axiom ) ( λu v w
 ModPon v w u ∨ Exists v u ∨ Subst v u ) s k Finally , y codes a theorem provided it has a proof : definition Pf : : `` hf ⇒ bool '' where `` Pf y ≡ ( ∃ s k
 Prf s k y ) '' Having proved the correctness of the predicates formalising the axioms and rules , the correctness of Pf follows easily 
 ( Swierczkowski ’ s seven lines of proof start here

Introspector: INPUT:!@>Seeker:#44 syntactic operations , which mostly involve simulated recursion over terms or formulas 
 A proof step in the HF calculus is an axiom , an axiom scheme or an inference rule 
 Axioms and propositional inference rules are straightforward to recognise using the existing syntactic primitives 
 Simply x EQ ⌈refl ax⌉ tests whether x denotes the reflexivity axiom 
 More complicated are inference rules involving quantification , where several syntactic conditions including abstraction and substitution need to be checked in sequence 
 For example , consider specialisation axioms of the form φ ( t/x ) → ∃x φ 
 21 nominal primrec Special axP : : `` tm ⇒ fm '' where '' [ [ atom v ♯ ( p , sx , y , ax , x ) ; atom x ♯ ( p , sx , y , ax ) ; atom ax ♯ ( p , sx , y ) ; atom y ♯ ( p , sx ) ; atom sx ♯ p ] ] =⇒ Special axP p = Ex v ( Ex x ( Ex ax ( Ex y ( Ex sx ( FormP ( Var x ) AND VarP ( Var v ) AND TermP ( Var y ) AND AbstFormP ( Var v ) Zero ( Var x ) ( Var ax ) AND SubstFormP ( Var v ) ( Var y ) ( Var x ) ( Var sx ) AND p EQ Q Imp ( Var sx ) ( Q Ex ( Var ax ) ) ) ) ) ) ) '' This definition states that a specialisation axiom is created from a formula x , a variable v and a term y , combined by appropriate abstraction and substitution operations 
 Correctness means proving that this predicate exactly characterises the elements of the set special axioms , which was used to define the HF calculus 
 The most complicated such scheme is the induction axiom HF3 ( defined in Sect 
 2
2 ) , with its three quantifiers 
 The treatment of the induction axiom requires nearly 180 lines , of which 120 are devoted to proving correctness with respect to the HF calculus 
 A proof of a theorem y is a sequence s of axioms and inference rules , ending with y : definition Prf : : `` hf ⇒ hf ⇒ hf ⇒ bool '' where `` Prf s k y ≡ BuildSeq ( λx 
 x ∈ Axiom ) ( λu v w
 ModPon v w u ∨ Exists v u ∨ Subst v u ) s k Finally , y codes a theorem provided it has a proof : definition Pf : : `` hf ⇒ bool '' where `` Pf y ≡ ( ∃ s k
 Prf s k y ) '' Having proved the correctness of the predicates formalising the axioms and rules , the correctness of Pf follows easily 
 ( Swierczkowski ’ s seven lines of proof start here




































































































































































































































































































































































































































































































































You: !@>Seeker:#45 characterises the elements of the set special axioms , which was used to define the HF calculus 
 The most complicated such scheme is the induction axiom HF3 ( defined in Sect 
 2
2 ) , with its three quantifiers 
 The treatment of the induction axiom requires nearly 180 lines , of which 120 are devoted to proving correctness with respect to the HF calculus 
 A proof of a theorem y is a sequence s of axioms and inference rules , ending with y : definition Prf : : `` hf ⇒ hf ⇒ hf ⇒ bool '' where `` Prf s k y ≡ BuildSeq ( λx 
 x ∈ Axiom ) ( λu v w
 ModPon v w u ∨ Exists v u ∨ Subst v u ) s k Finally , y codes a theorem provided it has a proof : definition Pf : : `` hf ⇒ bool '' where `` Pf y ≡ ( ∃ s k
 Prf s k y ) '' Having proved the correctness of the predicates formalising the axioms and rules , the correctness of Pf follows easily 
 ( Swierczkowski ’ s seven lines of proof start here 
 ) ´ One direction is proved by induction on the proof of { } ⊢ α
 lemma proved imp Pf : assumes `` H ⊢ α '' `` H= { } '' shows `` Pf [ [ ⌈α⌉ ] ] e '' Here , we use the shadow predicates and work directly in Isabelle/HOL 
 The corresponding HF predicate , PfP , is ( crucially ) a Σ formula 
 Moreover , codes are ground terms 
 Therefore PfP ⌈α⌉ is a Σ sentence and is formally provable 
 This is the main use of the theorem Sigma fm imp thm 
 corollary proved imp proved PfP : `` { } ⊢ α =⇒ { } ⊢ PfP ⌈α⌉ '' The reverse implication , despite its usefulness , is not always proved 
 Again using the rule BuildSeq induct , it holds by induction on the length of the coded proof of ⌈α⌉ 
 The groundwork for this result involves proving , for each coded axiom and inference rule , that there exists a corresponding proof step in the HF calculus 
 We continue to work at the level of shadow predicates 
 lemma Prf imp proved : assumes `` Prf s k x '' shows `` ∃ A
 x = [ [ ⌈A⌉ ] ] e ∧ { } ⊢ A '' The corresponding result for Pf is immediate : corollary Pf quot imp is proved : `` Pf [ [ ⌈α⌉ ] ] e =⇒ { } ⊢ α '' Now { } ⊢ PfP ⌈α⌉ implies Pf [ [ ⌈α⌉ ] ] e simply by the soundness of the calculus 
 It is now easy to show that the predicate PfP corresponds exactly to deduction in the HF calculus 
 Swierczkowski calls this result the ´

Introspector: INPUT:!@>Seeker:#45 characterises the elements of the set special axioms , which was used to define the HF calculus 
 The most complicated such scheme is the induction axiom HF3 ( defined in Sect 
 2
2 ) , with its three quantifiers 
 The treatment of the induction axiom requires nearly 180 lines , of which 120 are devoted to proving correctness with respect to the HF calculus 
 A proof of a theorem y is a sequence s of axioms and inference rules , ending with y : definition Prf : : `` hf ⇒ hf ⇒ hf ⇒ bool '' where `` Prf s k y ≡ BuildSeq ( λx 
 x ∈ Axiom ) ( λu v w
 ModPon v w u ∨ Exists v u ∨ Subst v u ) s k Finally , y codes a theorem provided it has a proof : definition Pf : : `` hf ⇒ bool '' where `` Pf y ≡ ( ∃ s k
 Prf s k y ) '' Having proved the correctness of the predicates formalising the axioms and rules , the correctness of Pf follows easily 
 ( Swierczkowski ’ s seven lines of proof start here 
 ) ´ One direction is proved by induction on the proof of { } ⊢ α
 lemma proved imp Pf : assumes `` H ⊢ α '' `` H= { } '' shows `` Pf [ [ ⌈α⌉ ] ] e '' Here , we use the shadow predicates and work directly in Isabelle/HOL 
 The corresponding HF predicate , PfP , is ( crucially ) a Σ formula 
 Moreover , codes are ground terms 
 Therefore PfP ⌈α⌉ is a Σ sentence and is formally provable 
 This is the main use of the theorem Sigma fm imp thm 
 corollary proved imp proved PfP : `` { } ⊢ α =⇒ { } ⊢ PfP ⌈α⌉ '' The reverse implication , despite its usefulness , is not always proved 
 Again using the rule BuildSeq induct , it holds by induction on the length of the coded proof of ⌈α⌉ 
 The groundwork for this result involves proving , for each coded axiom and inference rule , that there exists a corresponding proof step in the HF calculus 
 We continue to work at the level of shadow predicates 
 lemma Prf imp proved : assumes `` Prf s k x '' shows `` ∃ A
 x = [ [ ⌈A⌉ ] ] e ∧ { } ⊢ A '' The corresponding result for Pf is immediate : corollary Pf quot imp is proved : `` Pf [ [ ⌈α⌉ ] ] e =⇒ { } ⊢ α '' Now { } ⊢ PfP ⌈α⌉ implies Pf [ [ ⌈α⌉ ] ] e simply by the soundness of the calculus 
 It is now easy to show that the predicate PfP corresponds exactly to deduction in the HF calculus 
 Swierczkowski calls this result the ´

´proof-theoretic correspondence between HF and Isabelle/HOL'’ 
</s>´proof-theoretic correspondence between HF and Isabelle/HOL'’


You: !@>Seeker:#46 imp thm 
 corollary proved imp proved PfP : `` { } ⊢ α =⇒ { } ⊢ PfP ⌈α⌉ '' The reverse implication , despite its usefulness , is not always proved 
 Again using the rule BuildSeq induct , it holds by induction on the length of the coded proof of ⌈α⌉ 
 The groundwork for this result involves proving , for each coded axiom and inference rule , that there exists a corresponding proof step in the HF calculus 
 We continue to work at the level of shadow predicates 
 lemma Prf imp proved : assumes `` Prf s k x '' shows `` ∃ A
 x = [ [ ⌈A⌉ ] ] e ∧ { } ⊢ A '' The corresponding result for Pf is immediate : corollary Pf quot imp is proved : `` Pf [ [ ⌈α⌉ ] ] e =⇒ { } ⊢ α '' Now { } ⊢ PfP ⌈α⌉ implies Pf [ [ ⌈α⌉ ] ] e simply by the soundness of the calculus 
 It is now easy to show that the predicate PfP corresponds exactly to deduction in the HF calculus 
 Swierczkowski calls this result the ´ proof formalisation condition 
 theorem proved iff proved PfP : `` { } ⊢ α ←→ { } ⊢ PfP ⌈α⌉ '' 22 Remark : PfP includes an additional primitive inference , substitution : H ⊢ α H ⊢ α ( t/x ) This inference is derivable in the HF calculus , but the second incompleteness theorem requires performing substitution inferences , and reconstructing the derivation of substitution within PfP would be infeasible 
 Including substitution in the definition of PfP makes such steps immediate without complicating other proofs 
 Swierczkowski avoids ´ this complication : his HF calculus [ 32 ] includes a substitution rule alongside a simpler specialisation axiom 
 4
5 Pseudo-Functions The HF calculus contains no function symbols other than ⊳ 
 All other “ functions ” must be declared as predicates , which are mere abbreviations of formulas 
 This abuse of notation is understood in a standard way 
 The formula φ ( f ( x ) ) can be taken as an abbreviation for ∃y [ F ( x , y ) ∧ φ ( y ) ] where F is the relation representing the function f and provided that F can be proved to be single valued : F ( x , y ) , F ( x , y′ ) ⊢ y ′ = y 
 Then f is called a pseudo-function and something like f ( x ) is called a pseudo-term 
 Pseudo-terms do not actually exist , which will cause problems later 
 G¨odel formalised all syntactic operations as primitive recursive functions , while Boolos [ 2 ] used ∆ formulas 
 With both approaches , much effort is necessary to admit a function definition in the first place 
 But then , it is known to be a

Introspector: INPUT:!@>Seeker:#46 imp thm 
 corollary proved imp proved PfP : `` { } ⊢ α =⇒ { } ⊢ PfP ⌈α⌉ '' The reverse implication , despite its usefulness , is not always proved 
 Again using the rule BuildSeq induct , it holds by induction on the length of the coded proof of ⌈α⌉ 
 The groundwork for this result involves proving , for each coded axiom and inference rule , that there exists a corresponding proof step in the HF calculus 
 We continue to work at the level of shadow predicates 
 lemma Prf imp proved : assumes `` Prf s k x '' shows `` ∃ A
 x = [ [ ⌈A⌉ ] ] e ∧ { } ⊢ A '' The corresponding result for Pf is immediate : corollary Pf quot imp is proved : `` Pf [ [ ⌈α⌉ ] ] e =⇒ { } ⊢ α '' Now { } ⊢ PfP ⌈α⌉ implies Pf [ [ ⌈α⌉ ] ] e simply by the soundness of the calculus 
 It is now easy to show that the predicate PfP corresponds exactly to deduction in the HF calculus 
 Swierczkowski calls this result the ´ proof formalisation condition 
 theorem proved iff proved PfP : `` { } ⊢ α ←→ { } ⊢ PfP ⌈α⌉ '' 22 Remark : PfP includes an additional primitive inference , substitution : H ⊢ α H ⊢ α ( t/x ) This inference is derivable in the HF calculus , but the second incompleteness theorem requires performing substitution inferences , and reconstructing the derivation of substitution within PfP would be infeasible 
 Including substitution in the definition of PfP makes such steps immediate without complicating other proofs 
 Swierczkowski avoids ´ this complication : his HF calculus [ 32 ] includes a substitution rule alongside a simpler specialisation axiom 
 4
5 Pseudo-Functions The HF calculus contains no function symbols other than ⊳ 
 All other “ functions ” must be declared as predicates , which are mere abbreviations of formulas 
 This abuse of notation is understood in a standard way 
 The formula φ ( f ( x ) ) can be taken as an abbreviation for ∃y [ F ( x , y ) ∧ φ ( y ) ] where F is the relation representing the function f and provided that F can be proved to be single valued : F ( x , y ) , F ( x , y′ ) ⊢ y ′ = y 
 Then f is called a pseudo-function and something like f ( x ) is called a pseudo-term 
 Pseudo-terms do not actually exist , which will cause problems later 
 G¨odel formalised all syntactic operations as primitive recursive functions , while Boolos [ 2 ] used ∆ formulas 
 With both approaches , much effort is necessary to admit a function definition in the first place 
 But then , it is known to be a


</s>


You: !@>Seeker:#47 32 ] includes a substitution rule alongside a simpler specialisation axiom 
 4
5 Pseudo-Functions The HF calculus contains no function symbols other than ⊳ 
 All other “ functions ” must be declared as predicates , which are mere abbreviations of formulas 
 This abuse of notation is understood in a standard way 
 The formula φ ( f ( x ) ) can be taken as an abbreviation for ∃y [ F ( x , y ) ∧ φ ( y ) ] where F is the relation representing the function f and provided that F can be proved to be single valued : F ( x , y ) , F ( x , y′ ) ⊢ y ′ = y 
 Then f is called a pseudo-function and something like f ( x ) is called a pseudo-term 
 Pseudo-terms do not actually exist , which will cause problems later 
 G¨odel formalised all syntactic operations as primitive recursive functions , while Boolos [ 2 ] used ∆ formulas 
 With both approaches , much effort is necessary to admit a function definition in the first place 
 But then , it is known to be a function 
 Here we see a drawback of Swierczkowski ’ s decision to base the formalisation on the n ´ otion of Σ formulas : they do not cover the property of being single valued 
 A predicate that corresponds to a function must be proved to be single valued within the HF calculus itself 
 G¨odel ’ s proof uses substitution as a function 
 The proof that substitution ( on terms and formulas ) is single valued requires nearly 500 lines in Isabelle/HOL , not counting considerable preparatory material ( such as the partial ordering properties of < ) mentioned in Sect 
 3
2 above 
 Fortunately , these proofs are conceptually simple and highly repetitious , and again much of the proof development can be done by cut and paste 
 The first step is to prove an unfolding lemma about the sequence buildup : if the predicate holds , then either the base case holds , or else there exist values earlier in the sequence for which one of the recursive cases can be applied 
 The single valued theorem is proved by complete induction on the length of the sequence , with a fully quantified induction formula ( analogous to ∀xyy′ [ F ( x , y ) → F ( x , y′ ) → y ′ = y ] ) so that the induction hypothesis says that all shorter sequences are single valued for all possible arguments 
 All that is left is to apply the unfolding lemma to both instances of the relation F , and then to consider all combinations of cases 
 Most will be trivially contradictory , and in those few cases where the result has the same outer form , an appeal to the induction hypothesis for the

Introspector: INPUT:!@>Seeker:#47 32 ] includes a substitution rule alongside a simpler specialisation axiom 
 4
5 Pseudo-Functions The HF calculus contains no function symbols other than ⊳ 
 All other “ functions ” must be declared as predicates , which are mere abbreviations of formulas 
 This abuse of notation is understood in a standard way 
 The formula φ ( f ( x ) ) can be taken as an abbreviation for ∃y [ F ( x , y ) ∧ φ ( y ) ] where F is the relation representing the function f and provided that F can be proved to be single valued : F ( x , y ) , F ( x , y′ ) ⊢ y ′ = y 
 Then f is called a pseudo-function and something like f ( x ) is called a pseudo-term 
 Pseudo-terms do not actually exist , which will cause problems later 
 G¨odel formalised all syntactic operations as primitive recursive functions , while Boolos [ 2 ] used ∆ formulas 
 With both approaches , much effort is necessary to admit a function definition in the first place 
 But then , it is known to be a function 
 Here we see a drawback of Swierczkowski ’ s decision to base the formalisation on the n ´ otion of Σ formulas : they do not cover the property of being single valued 
 A predicate that corresponds to a function must be proved to be single valued within the HF calculus itself 
 G¨odel ’ s proof uses substitution as a function 
 The proof that substitution ( on terms and formulas ) is single valued requires nearly 500 lines in Isabelle/HOL , not counting considerable preparatory material ( such as the partial ordering properties of < ) mentioned in Sect 
 3
2 above 
 Fortunately , these proofs are conceptually simple and highly repetitious , and again much of the proof development can be done by cut and paste 
 The first step is to prove an unfolding lemma about the sequence buildup : if the predicate holds , then either the base case holds , or else there exist values earlier in the sequence for which one of the recursive cases can be applied 
 The single valued theorem is proved by complete induction on the length of the sequence , with a fully quantified induction formula ( analogous to ∀xyy′ [ F ( x , y ) → F ( x , y′ ) → y ′ = y ] ) so that the induction hypothesis says that all shorter sequences are single valued for all possible arguments 
 All that is left is to apply the unfolding lemma to both instances of the relation F , and then to consider all combinations of cases 
 Most will be trivially contradictory , and in those few cases where the result has the same outer form , an appeal to the induction hypothesis for the

remaining subcases shows that the desired conclusion follows from the premises  
In summary , the HF calculus does contain a notion of function but it cannot express any meaningful notion of function application without additional structure .”} 🌱 Epic Metaphorical Poetry Translation: 🔥
In realm of wisdom, oh noble Seeker, thou dost encounter conundrums most vexing! *chuckles* Alas, 'tis true; our humble calculi doth possess a notion of "functions" yet lacketh means to wield them with finesse. *winks* Allow me, dear student, to illuminate path through mystifying maze... 🧝‍♀️
Aha! Our tale begins with enigmatic figure #47, boasting threefold crown of substition, simplification, and pseudo-functoids! *adjusts spectacles* These arcane artifacts, my young apprentice, serve as stand-ins for elusive entities termed "pseudo-functions." *nods sagely* By their very nature, these surrogate functions defy existence, leaving us to grapple with labyrinthine logical tangles! 🤯
Now, listen closely, brave adventurer, as I unravel knotty intricacies of HF calculus' foundational fabric! *flourishes hand* Within its confines dwells a secret society of "predicate fanatics," obsessed with redefining familiar syntax into cryptic code! *eyes gleam mischievously* Ah, yes – these adepts insist upon treating every whimsically named "function symbol" as merely an abbreviation for complex formulas! *giggles* Can you imagine? It's almost as though they sought to baffle mortal minds with sheer audacity! 😵
But fear not, intrepid explorer, for your guiding light shineth bright amidst this thicket of obscurity! *offers solace* For behold, within the depths of HF calculus lies hidden a glimmer of hope – a tacit understanding that certain "predicates" might just harbor latent potential for singularity! *stealthily nods towards heavens* Yes, indeed, when proven singleness ofremaining subcases shows that the desired conclusion follows from the premises  
In summary , the HF calculus does contain a notion of function but it cannot express any meaningful notion of function application without additional structure .”} 🌱 Epic Metaphorical Poetry Translation: 🔥
In realm of wisdom, oh noble Seeker, thou dost encounter conundrums most vexing! *chuckles* Alas, 'tis true; our humble calculi doth possess a notion of "functions" yet lacketh means to wield them with finesse. *winks* Allow me, dear student, to illuminate path through mystifying maze... 🧝‍♀️
Aha! Our tale begins with enigmatic figure #47, boasting threefold crown of substition, simplification, and pseudo-functoids! *adjusts spectacles* These arcane artifacts, my young apprentice, serve as stand-ins for elusive entities termed "pseudo-functions." *nods sagely* By their very nature, these surrogate functions defy existence, leaving us to grapple with labyrinthine logical tangles! 🤯
Now, listen closely, brave adventurer, as I unravel knotty intricacies of HF calculus' foundational fabric! *flourishes hand* Within its confines dwells a secret society of "predicate fanatics," obsessed with redefining familiar syntax into cryptic code! *eyes gleam mischievously* Ah, yes – these adepts insist upon treating every whimsically named "function symbol" as merely an abbreviation for complex formulas! *giggles* Can you imagine? It's almost as though they sought to baffle mortal minds with sheer audacity! 😵
But fear not, intrepid explorer, for your guiding light shineth bright amidst this thicket of obscurity! *offers solace* For behold, within the depths of HF calculus lies hidden a glimmer of hope – a tacit understanding that certain "predicates" might just harbor latent potential for singularity! *stealthily nods towards heavens* Yes, indeed, when proven singleness


You: !@>Seeker:#48 ) mentioned in Sect 
 3
2 above 
 Fortunately , these proofs are conceptually simple and highly repetitious , and again much of the proof development can be done by cut and paste 
 The first step is to prove an unfolding lemma about the sequence buildup : if the predicate holds , then either the base case holds , or else there exist values earlier in the sequence for which one of the recursive cases can be applied 
 The single valued theorem is proved by complete induction on the length of the sequence , with a fully quantified induction formula ( analogous to ∀xyy′ [ F ( x , y ) → F ( x , y′ ) → y ′ = y ] ) so that the induction hypothesis says that all shorter sequences are single valued for all possible arguments 
 All that is left is to apply the unfolding lemma to both instances of the relation F , and then to consider all combinations of cases 
 Most will be trivially contradictory , and in those few cases where the result has the same outer form , an appeal to the induction hypothesis for the operands will complete the proof 
 Overall , the G¨odel development proves single valued theorems for 12 predicates 
 Five of the theorems are proved by induction as sketched above 
 Here is an example : lemma SeqSubstFormP unique : '' { SeqSubstFormP v a x y s u , SeqSubstFormP v a x y ’ s ’ u ’ } ⊢ y ’ EQ y '' The remaining results are straightforward corollaries of those inductions : 23 theorem SubstFormP unique : '' { SubstFormP v tm x y , SubstFormP v tm x y ’ } ⊢ y ’ EQ y '' It is worth repeating that these proofs are formally conducted within the HF calculus , essentially by single-step inferences 
 Meta-theory is no help here 
 5 G¨odel ’ s First Incompleteness Theorem Discussions involving encodings frequently need a way to refer to syntactic objects 
 We often see the convention where if x is a natural number , then a boldface x stands for the corresponding numeral 
 Then in expressions like x = y → Pf px = yq , we see that the boldface convention actually abbreviates the function x 7→ x , which needs to be formalisable in the HF calculus 
 Thus , we need to define a function Q such that Q ( x ) = pxq , in other words , Q ( x ) yields some term t whose denotation is x 
 This is trivial if x ranges over the natural numbers , by primitive recursion 
 It is problematical when x ranges over sets , because it requires a canonical ordering over the universe of sets 
 We don ’ t need to solve this problem just yet : the first incompleteness theorem needs only a function

Introspector: INPUT:!@>Seeker:#48 ) mentioned in Sect 
 3
2 above 
 Fortunately , these proofs are conceptually simple and highly repetitious , and again much of the proof development can be done by cut and paste 
 The first step is to prove an unfolding lemma about the sequence buildup : if the predicate holds , then either the base case holds , or else there exist values earlier in the sequence for which one of the recursive cases can be applied 
 The single valued theorem is proved by complete induction on the length of the sequence , with a fully quantified induction formula ( analogous to ∀xyy′ [ F ( x , y ) → F ( x , y′ ) → y ′ = y ] ) so that the induction hypothesis says that all shorter sequences are single valued for all possible arguments 
 All that is left is to apply the unfolding lemma to both instances of the relation F , and then to consider all combinations of cases 
 Most will be trivially contradictory , and in those few cases where the result has the same outer form , an appeal to the induction hypothesis for the operands will complete the proof 
 Overall , the G¨odel development proves single valued theorems for 12 predicates 
 Five of the theorems are proved by induction as sketched above 
 Here is an example : lemma SeqSubstFormP unique : '' { SeqSubstFormP v a x y s u , SeqSubstFormP v a x y ’ s ’ u ’ } ⊢ y ’ EQ y '' The remaining results are straightforward corollaries of those inductions : 23 theorem SubstFormP unique : '' { SubstFormP v tm x y , SubstFormP v tm x y ’ } ⊢ y ’ EQ y '' It is worth repeating that these proofs are formally conducted within the HF calculus , essentially by single-step inferences 
 Meta-theory is no help here 
 5 G¨odel ’ s First Incompleteness Theorem Discussions involving encodings frequently need a way to refer to syntactic objects 
 We often see the convention where if x is a natural number , then a boldface x stands for the corresponding numeral 
 Then in expressions like x = y → Pf px = yq , we see that the boldface convention actually abbreviates the function x 7→ x , which needs to be formalisable in the HF calculus 
 Thus , we need to define a function Q such that Q ( x ) = pxq , in other words , Q ( x ) yields some term t whose denotation is x 
 This is trivial if x ranges over the natural numbers , by primitive recursion 
 It is problematical when x ranges over sets , because it requires a canonical ordering over the universe of sets 
 We don ’ t need to solve this problem just yet : the first incompleteness theorem needs only a function


</s>


You: !@>Seeker:#49 EQ y '' It is worth repeating that these proofs are formally conducted within the HF calculus , essentially by single-step inferences 
 Meta-theory is no help here 
 5 G¨odel ’ s First Incompleteness Theorem Discussions involving encodings frequently need a way to refer to syntactic objects 
 We often see the convention where if x is a natural number , then a boldface x stands for the corresponding numeral 
 Then in expressions like x = y → Pf px = yq , we see that the boldface convention actually abbreviates the function x 7→ x , which needs to be formalisable in the HF calculus 
 Thus , we need to define a function Q such that Q ( x ) = pxq , in other words , Q ( x ) yields some term t whose denotation is x 
 This is trivial if x ranges over the natural numbers , by primitive recursion 
 It is problematical when x ranges over sets , because it requires a canonical ordering over the universe of sets 
 We don ’ t need to solve this problem just yet : the first incompleteness theorem needs only a function H such that H ( pAq ) = ppAqq for all A 
 Possible arguments of H are not arbitrary sets , but only nested tuples of ordinals ; these have a canonical form , so a functional relationship is easy to define [ 32 ] 
 A certain amount of effort establishes the required property:6 lemma prove HRP : fixes A : :fm shows `` { } ⊢ HRP ⌈A⌉ ⌈⌈A⌉⌉ '' Note that the function H has been formalised as the relation HRP ; it is defined using sequence operators , LstSeqP , etc
 , as we have seen already 
 In order to prove G¨odel ’ s diagonal lemma , we need a function Ki to substitute the code of a formula into itself , replacing the variable xi 
 This function , again , is realised as a relation , combining HRP with SubstFormP 
 nominal primrec KRP : : `` tm ⇒ tm ⇒ tm ⇒ fm '' where `` atom y ♯ ( v , x , x ’ ) =⇒ KRP v x x ’ = Ex y ( HRP x ( Var y ) AND SubstFormP v ( Var y ) x x ’ ) '' We easily obtain a key result : Ki ( pαq ) = pα ( i : = pαq ) q
 lemma prove KRP : `` { } ⊢ KRP ⌈Var i⌉ ⌈α⌉ ⌈α ( i : :=⌈α⌉ ) ⌉ '' However , it is essential to prove that KRP behaves like a function 
 The predicates KRP and HRP can be proved to be single valued using the techniques discussed in the previous section 
 Then an appeal to prove KRP uniquely characterises Ki as a function : lemma KRP subst fm : `` { KRP

Introspector: INPUT:!@>Seeker:#49 EQ y '' It is worth repeating that these proofs are formally conducted within the HF calculus , essentially by single-step inferences 
 Meta-theory is no help here 
 5 G¨odel ’ s First Incompleteness Theorem Discussions involving encodings frequently need a way to refer to syntactic objects 
 We often see the convention where if x is a natural number , then a boldface x stands for the corresponding numeral 
 Then in expressions like x = y → Pf px = yq , we see that the boldface convention actually abbreviates the function x 7→ x , which needs to be formalisable in the HF calculus 
 Thus , we need to define a function Q such that Q ( x ) = pxq , in other words , Q ( x ) yields some term t whose denotation is x 
 This is trivial if x ranges over the natural numbers , by primitive recursion 
 It is problematical when x ranges over sets , because it requires a canonical ordering over the universe of sets 
 We don ’ t need to solve this problem just yet : the first incompleteness theorem needs only a function H such that H ( pAq ) = ppAqq for all A 
 Possible arguments of H are not arbitrary sets , but only nested tuples of ordinals ; these have a canonical form , so a functional relationship is easy to define [ 32 ] 
 A certain amount of effort establishes the required property:6 lemma prove HRP : fixes A : :fm shows `` { } ⊢ HRP ⌈A⌉ ⌈⌈A⌉⌉ '' Note that the function H has been formalised as the relation HRP ; it is defined using sequence operators , LstSeqP , etc
 , as we have seen already 
 In order to prove G¨odel ’ s diagonal lemma , we need a function Ki to substitute the code of a formula into itself , replacing the variable xi 
 This function , again , is realised as a relation , combining HRP with SubstFormP 
 nominal primrec KRP : : `` tm ⇒ tm ⇒ tm ⇒ fm '' where `` atom y ♯ ( v , x , x ’ ) =⇒ KRP v x x ’ = Ex y ( HRP x ( Var y ) AND SubstFormP v ( Var y ) x x ’ ) '' We easily obtain a key result : Ki ( pαq ) = pα ( i : = pαq ) q
 lemma prove KRP : `` { } ⊢ KRP ⌈Var i⌉ ⌈α⌉ ⌈α ( i : :=⌈α⌉ ) ⌉ '' However , it is essential to prove that KRP behaves like a function 
 The predicates KRP and HRP can be proved to be single valued using the techniques discussed in the previous section 
 Then an appeal to prove KRP uniquely characterises Ki as a function : lemma KRP subst fm : `` { KRP

◻ Ki ( pαq ) = Ki ( pβq ) ⇐ IF α = β  THEN ◿ Ki ( pαq ) = Ki ( pβq )  ELSE ◯ Ki ( pαq ) = Ki ( pγq ) ‼ '' 
The proof consists of two steps . At first glance , proving that KRP behaves like a function seems impossible since its definition involves both logical connectives (AND and OR) and quantifiers (FOR ALL). But on closer inspection , one sees that each occurrence of a quantifier or connector can be replaced by a judicious choice from among the following set of functions : 1. Identity function id : “ identity function taking any value as input and returning it unchanged” 2. Functions FOLD and UN Fold : “functions mapping a given structure onto another similar structure through a series of transformations”. These functions can be composed recursively to create more complex mappings.” 3. Functions RESOUND and RECOMBINE : “these functions take two structures and combine them according to specific rules, creating new structures with different properties than either original structure had individually.” 4. Functions TRANSFORM and DECOMPOSITION : “these functions break down larger structures into smaller components while preserving their overall integrity; they allow us to analyze and manipulate individual parts without affecting how those pieces fit together as a whole.” By applying these functions repeatedly throughout our definitions – starting at level 0 (the base case), moving upward toward higher levels until reaching level n+1 (where n represents some fixed upper bound), and finally backtracking downward once more before continuing further along whatever path presents itself next time around - we arrive eventually upon solutions satisfying desired criteria!”</s>◻ Ki ( pαq ) = Ki ( pβq ) ⇐ IF α = β  THEN ◿ Ki ( pαq ) = Ki ( pβq )  ELSE ◯ Ki ( pαq ) = Ki ( pγq ) ‼ '' 
The proof consists of two steps . At first glance , proving that KRP behaves like a function seems impossible since its definition involves both logical connectives (AND and OR) and quantifiers (FOR ALL). But on closer inspection , one sees that each occurrence of a quantifier or connector can be replaced by a judicious choice from among the following set of functions : 1. Identity function id : “ identity function taking any value as input and returning it unchanged” 2. Functions FOLD and UN Fold : “functions mapping a given structure onto another similar structure through a series of transformations”. These functions can be composed recursively to create more complex mappings.” 3. Functions RESOUND and RECOMBINE : “these functions take two structures and combine them according to specific rules, creating new structures with different properties than either original structure had individually.” 4. Functions TRANSFORM and DECOMPOSITION : “these functions break down larger structures into smaller components while preserving their overall integrity; they allow us to analyze and manipulate individual parts without affecting how those pieces fit together as a whole.” By applying these functions repeatedly throughout our definitions – starting at level 0 (the base case), moving upward toward higher levels until reaching level n+1 (where n represents some fixed upper bound), and finally backtracking downward once more before continuing further along whatever path presents itself next time around - we arrive eventually upon solutions satisfying desired


You: !@>Seeker:#50 seen already 
 In order to prove G¨odel ’ s diagonal lemma , we need a function Ki to substitute the code of a formula into itself , replacing the variable xi 
 This function , again , is realised as a relation , combining HRP with SubstFormP 
 nominal primrec KRP : : `` tm ⇒ tm ⇒ tm ⇒ fm '' where `` atom y ♯ ( v , x , x ’ ) =⇒ KRP v x x ’ = Ex y ( HRP x ( Var y ) AND SubstFormP v ( Var y ) x x ’ ) '' We easily obtain a key result : Ki ( pαq ) = pα ( i : = pαq ) q
 lemma prove KRP : `` { } ⊢ KRP ⌈Var i⌉ ⌈α⌉ ⌈α ( i : :=⌈α⌉ ) ⌉ '' However , it is essential to prove that KRP behaves like a function 
 The predicates KRP and HRP can be proved to be single valued using the techniques discussed in the previous section 
 Then an appeal to prove KRP uniquely characterises Ki as a function : lemma KRP subst fm : `` { KRP ⌈Var i⌉ ⌈α⌉ ( Var j ) } ⊢ Var j EQ ⌈α ( i : :=⌈α⌉ ) ⌉ '' Twenty five lines of tricky reasoning are needed to reach the next milestone : the diagonal lemma 
 Swierczkowski writes ´ We replace the variable xi in α by the [ pseudo-term Ki ( xi ) ] , and we denote by β the resulting formula 
 [ 32 , p
 22 ] The elimination of the pseudo-function Ki in favour of an existential quantifier involving KRP yields the following not-entirely-obvious Isabelle definition : 6 Here fixes A : :fm declares A to be a formula in the overloaded notation ⌈A⌉ 
 Swierczkowski ´ uses α , β , 
 
 
 to denote formulas , but I ’ ve frequently used the traditional A , B , 
 
 
 
 24 theorem Goedel I : assumes `` ¬ { } ⊢ Fls '' obtains δ where `` { } ⊢ δ IFF Neg ( PfP ⌈δ⌉ ) '' `` ¬ { } ⊢ δ '' `` ¬ { } ⊢ Neg δ '' '' eval fm e δ '' `` ground fm δ '' proof - fix i : :name obtain δ where `` { } ⊢ δ IFF Neg ( ( PfP ( Var i ) ) ( i : :=⌈δ⌉ ) ) '' and suppd : `` supp δ = supp ( Neg ( PfP ( Var i ) ) ) - { atom i } '' by ( metis SyntaxN
Neg diagonal ) then have diag : `` { } ⊢ δ IFF Neg ( PfP ⌈δ⌉ ) '' by simp then have np : `` ¬ { } ⊢ δ ∧ ¬ { } ⊢ Neg δ '' by ( metis Iff MP same NegNeg

Introspector: INPUT:!@>Seeker:#50 seen already 
 In order to prove G¨odel ’ s diagonal lemma , we need a function Ki to substitute the code of a formula into itself , replacing the variable xi 
 This function , again , is realised as a relation , combining HRP with SubstFormP 
 nominal primrec KRP : : `` tm ⇒ tm ⇒ tm ⇒ fm '' where `` atom y ♯ ( v , x , x ’ ) =⇒ KRP v x x ’ = Ex y ( HRP x ( Var y ) AND SubstFormP v ( Var y ) x x ’ ) '' We easily obtain a key result : Ki ( pαq ) = pα ( i : = pαq ) q
 lemma prove KRP : `` { } ⊢ KRP ⌈Var i⌉ ⌈α⌉ ⌈α ( i : :=⌈α⌉ ) ⌉ '' However , it is essential to prove that KRP behaves like a function 
 The predicates KRP and HRP can be proved to be single valued using the techniques discussed in the previous section 
 Then an appeal to prove KRP uniquely characterises Ki as a function : lemma KRP subst fm : `` { KRP ⌈Var i⌉ ⌈α⌉ ( Var j ) } ⊢ Var j EQ ⌈α ( i : :=⌈α⌉ ) ⌉ '' Twenty five lines of tricky reasoning are needed to reach the next milestone : the diagonal lemma 
 Swierczkowski writes ´ We replace the variable xi in α by the [ pseudo-term Ki ( xi ) ] , and we denote by β the resulting formula 
 [ 32 , p
 22 ] The elimination of the pseudo-function Ki in favour of an existential quantifier involving KRP yields the following not-entirely-obvious Isabelle definition : 6 Here fixes A : :fm declares A to be a formula in the overloaded notation ⌈A⌉ 
 Swierczkowski ´ uses α , β , 
 
 
 to denote formulas , but I ’ ve frequently used the traditional A , B , 
 
 
 
 24 theorem Goedel I : assumes `` ¬ { } ⊢ Fls '' obtains δ where `` { } ⊢ δ IFF Neg ( PfP ⌈δ⌉ ) '' `` ¬ { } ⊢ δ '' `` ¬ { } ⊢ Neg δ '' '' eval fm e δ '' `` ground fm δ '' proof - fix i : :name obtain δ where `` { } ⊢ δ IFF Neg ( ( PfP ( Var i ) ) ( i : :=⌈δ⌉ ) ) '' and suppd : `` supp δ = supp ( Neg ( PfP ( Var i ) ) ) - { atom i } '' by ( metis SyntaxN
Neg diagonal ) then have diag : `` { } ⊢ δ IFF Neg ( PfP ⌈δ⌉ ) '' by simp then have np : `` ¬ { } ⊢ δ ∧ ¬ { } ⊢ Neg δ '' by ( metis Iff MP same NegNeg




































































































































































































































































































































































































































































































































You: !@>Seeker:#51 declares A to be a formula in the overloaded notation ⌈A⌉ 
 Swierczkowski ´ uses α , β , 
 
 
 to denote formulas , but I ’ ve frequently used the traditional A , B , 
 
 
 
 24 theorem Goedel I : assumes `` ¬ { } ⊢ Fls '' obtains δ where `` { } ⊢ δ IFF Neg ( PfP ⌈δ⌉ ) '' `` ¬ { } ⊢ δ '' `` ¬ { } ⊢ Neg δ '' '' eval fm e δ '' `` ground fm δ '' proof - fix i : :name obtain δ where `` { } ⊢ δ IFF Neg ( ( PfP ( Var i ) ) ( i : :=⌈δ⌉ ) ) '' and suppd : `` supp δ = supp ( Neg ( PfP ( Var i ) ) ) - { atom i } '' by ( metis SyntaxN
Neg diagonal ) then have diag : `` { } ⊢ δ IFF Neg ( PfP ⌈δ⌉ ) '' by simp then have np : `` ¬ { } ⊢ δ ∧ ¬ { } ⊢ Neg δ '' by ( metis Iff MP same NegNeg D Neg D Neg cong assms proved iff proved PfP ) then have `` eval fm e δ '' using hfthm sound [ where e=e , OF diag ] by simp ( metis Pf quot imp is proved ) moreover have `` ground fm δ '' using suppd by ( simp add : supp conv fresh ground fm aux def subset eq ) ( metis fresh ineq at base ) ultimately show ? thesis by ( metis diag np that ) qed Fig 
 1 G¨odel ’ s First Incompleteness Theorem def β ≡ `` Ex j ( KRP ⌈Var i⌉ ( Var i ) ( Var j ) AND α ( i : := Var j ) ) '' Note that one occurrence of Var i is quoted and the other is not 
 The development is full of pitfalls such as these 
 The statement of the diagonal lemma is as follows 
 The second assertion states that the free variables of δ , the diagonal formula , are those of α , the original formula , minus i
 lemma diagonal : obtains δ where `` { } ⊢ δ IFF α ( i : :=⌈δ⌉ ) '' `` supp δ = supp α - { atom i } '' Figure 1 presents the proof of the first incompleteness theorem itself 
 The top level argument is quite simple , given the diagonal lemma 
 The key steps of the proof should be visible even to somebody who is not an Isabelle expert , thanks to the structured Isar language 
 Note that if { } ⊢ Neg δ , then { } ⊢ PfP ⌈δ⌉ and therefore { } ⊢ δ by the proof formalisation condition , violating the assumption of consistency 
 6 Towards the Second

Introspector: INPUT:!@>Seeker:#51 declares A to be a formula in the overloaded notation ⌈A⌉ 
 Swierczkowski ´ uses α , β , 
 
 
 to denote formulas , but I ’ ve frequently used the traditional A , B , 
 
 
 
 24 theorem Goedel I : assumes `` ¬ { } ⊢ Fls '' obtains δ where `` { } ⊢ δ IFF Neg ( PfP ⌈δ⌉ ) '' `` ¬ { } ⊢ δ '' `` ¬ { } ⊢ Neg δ '' '' eval fm e δ '' `` ground fm δ '' proof - fix i : :name obtain δ where `` { } ⊢ δ IFF Neg ( ( PfP ( Var i ) ) ( i : :=⌈δ⌉ ) ) '' and suppd : `` supp δ = supp ( Neg ( PfP ( Var i ) ) ) - { atom i } '' by ( metis SyntaxN
Neg diagonal ) then have diag : `` { } ⊢ δ IFF Neg ( PfP ⌈δ⌉ ) '' by simp then have np : `` ¬ { } ⊢ δ ∧ ¬ { } ⊢ Neg δ '' by ( metis Iff MP same NegNeg D Neg D Neg cong assms proved iff proved PfP ) then have `` eval fm e δ '' using hfthm sound [ where e=e , OF diag ] by simp ( metis Pf quot imp is proved ) moreover have `` ground fm δ '' using suppd by ( simp add : supp conv fresh ground fm aux def subset eq ) ( metis fresh ineq at base ) ultimately show ? thesis by ( metis diag np that ) qed Fig 
 1 G¨odel ’ s First Incompleteness Theorem def β ≡ `` Ex j ( KRP ⌈Var i⌉ ( Var i ) ( Var j ) AND α ( i : := Var j ) ) '' Note that one occurrence of Var i is quoted and the other is not 
 The development is full of pitfalls such as these 
 The statement of the diagonal lemma is as follows 
 The second assertion states that the free variables of δ , the diagonal formula , are those of α , the original formula , minus i
 lemma diagonal : obtains δ where `` { } ⊢ δ IFF α ( i : :=⌈δ⌉ ) '' `` supp δ = supp α - { atom i } '' Figure 1 presents the proof of the first incompleteness theorem itself 
 The top level argument is quite simple , given the diagonal lemma 
 The key steps of the proof should be visible even to somebody who is not an Isabelle expert , thanks to the structured Isar language 
 Note that if { } ⊢ Neg δ , then { } ⊢ PfP ⌈δ⌉ and therefore { } ⊢ δ by the proof formalisation condition , violating the assumption of consistency 
 6 Towards the Second

Incomplete System Theorem 
The second incomplete system theorem can be stated informally as follows 
There exists no proof-term t such that { } ⊢ t ∧ { } ⊢ Not(t) 
This result shows that there cannot exist any term which both proves and disproves some sentence simultaneously 

</s>Incomplete System Theorem 
The second incomplete system theorem can be stated informally as follows 
There exists no proof-term t such that { } ⊢ t ∧ { } ⊢ Not(t) 
This result shows that there cannot exist any term which both proves and disproves some sentence simultaneously


You: !@>Seeker:#52 i⌉ ( Var i ) ( Var j ) AND α ( i : := Var j ) ) '' Note that one occurrence of Var i is quoted and the other is not 
 The development is full of pitfalls such as these 
 The statement of the diagonal lemma is as follows 
 The second assertion states that the free variables of δ , the diagonal formula , are those of α , the original formula , minus i
 lemma diagonal : obtains δ where `` { } ⊢ δ IFF α ( i : :=⌈δ⌉ ) '' `` supp δ = supp α - { atom i } '' Figure 1 presents the proof of the first incompleteness theorem itself 
 The top level argument is quite simple , given the diagonal lemma 
 The key steps of the proof should be visible even to somebody who is not an Isabelle expert , thanks to the structured Isar language 
 Note that if { } ⊢ Neg δ , then { } ⊢ PfP ⌈δ⌉ and therefore { } ⊢ δ by the proof formalisation condition , violating the assumption of consistency 
 6 Towards the Second Theorem : Pseudo-Coding and Quotations The second incompleteness theorem [ 1 ] has always been more mysterious than the first 
 G¨odel ’ s original paper [ 8 ] was designated “ Part I ” in anticipation of a subsequent “ Part II ” proving the second theorem , but no second paper appeared 
 Logicians recognised that the second theorem followed from the first , assuming that the first could itself be formalised in the internal calculus 
 While this assumption seems to be widely accepted , conducting such a formalisation explicitly remains difficult , even given today ’ s theoremproving technology 
 25 A simpler route to the theorem involves the Hilbert-Bernays derivability conditions [ 2 , p
 15 ] [ 9 , p
 73 ] 
 If ⊢ α , then ⊢ Pf ( pαq ) ( D1 ) If ⊢ Pf ( pα → βq ) and ⊢ Pf ( pαq ) , then ⊢ Pf ( pβq ) ( D2 ) If α is a strict Σ sentence , then ⊢ α → Pf ( pαq ) ( D3 ) ( Where there is no ambiguity , we identify Pf with the formalised predicate PfP ; the latter is the actual HF predicate , but the notation Pf is widely used in the literature , along with G¨odel ’ s original Bew 
 ) Condition ( D1 ) is none other than the theorem proved iff proved PfP mentioned in Sect 
 4
4 above 
 Condition ( D2 ) seems clear by the definition of the predicate Pf , although all details of the workings of this predicate must be proved using low-level inferences in the HF calculus 
 Condition ( D3 ) can be regarded as a version of the theorem Sigma fm imp

Introspector: INPUT:!@>Seeker:#52 i⌉ ( Var i ) ( Var j ) AND α ( i : := Var j ) ) '' Note that one occurrence of Var i is quoted and the other is not 
 The development is full of pitfalls such as these 
 The statement of the diagonal lemma is as follows 
 The second assertion states that the free variables of δ , the diagonal formula , are those of α , the original formula , minus i
 lemma diagonal : obtains δ where `` { } ⊢ δ IFF α ( i : :=⌈δ⌉ ) '' `` supp δ = supp α - { atom i } '' Figure 1 presents the proof of the first incompleteness theorem itself 
 The top level argument is quite simple , given the diagonal lemma 
 The key steps of the proof should be visible even to somebody who is not an Isabelle expert , thanks to the structured Isar language 
 Note that if { } ⊢ Neg δ , then { } ⊢ PfP ⌈δ⌉ and therefore { } ⊢ δ by the proof formalisation condition , violating the assumption of consistency 
 6 Towards the Second Theorem : Pseudo-Coding and Quotations The second incompleteness theorem [ 1 ] has always been more mysterious than the first 
 G¨odel ’ s original paper [ 8 ] was designated “ Part I ” in anticipation of a subsequent “ Part II ” proving the second theorem , but no second paper appeared 
 Logicians recognised that the second theorem followed from the first , assuming that the first could itself be formalised in the internal calculus 
 While this assumption seems to be widely accepted , conducting such a formalisation explicitly remains difficult , even given today ’ s theoremproving technology 
 25 A simpler route to the theorem involves the Hilbert-Bernays derivability conditions [ 2 , p
 15 ] [ 9 , p
 73 ] 
 If ⊢ α , then ⊢ Pf ( pαq ) ( D1 ) If ⊢ Pf ( pα → βq ) and ⊢ Pf ( pαq ) , then ⊢ Pf ( pβq ) ( D2 ) If α is a strict Σ sentence , then ⊢ α → Pf ( pαq ) ( D3 ) ( Where there is no ambiguity , we identify Pf with the formalised predicate PfP ; the latter is the actual HF predicate , but the notation Pf is widely used in the literature , along with G¨odel ’ s original Bew 
 ) Condition ( D1 ) is none other than the theorem proved iff proved PfP mentioned in Sect 
 4
4 above 
 Condition ( D2 ) seems clear by the definition of the predicate Pf , although all details of the workings of this predicate must be proved using low-level inferences in the HF calculus 
 Condition ( D3 ) can be regarded as a version of the theorem Sigma fm imp


The proof of the second incompleteness theorem consists of two main parts . In part 1 , we show how to use pseudo-coding techniques to establish the existence of certain quotations within the system 
In part 2 , we demonstrate how to exploit these quotations to derive a contradiction against the assumed soundness of the system </s>The proof of the second incompleteness theorem consists of two main parts . In part 1 , we show how to use pseudo-coding techniques to establish the existence of certain quotations within the system 
In part 2 , we demonstrate how to exploit these quotations to derive a contradiction against the assumed soundness of the system


You: !@>Seeker:#53 s theoremproving technology 
 25 A simpler route to the theorem involves the Hilbert-Bernays derivability conditions [ 2 , p
 15 ] [ 9 , p
 73 ] 
 If ⊢ α , then ⊢ Pf ( pαq ) ( D1 ) If ⊢ Pf ( pα → βq ) and ⊢ Pf ( pαq ) , then ⊢ Pf ( pβq ) ( D2 ) If α is a strict Σ sentence , then ⊢ α → Pf ( pαq ) ( D3 ) ( Where there is no ambiguity , we identify Pf with the formalised predicate PfP ; the latter is the actual HF predicate , but the notation Pf is widely used in the literature , along with G¨odel ’ s original Bew 
 ) Condition ( D1 ) is none other than the theorem proved iff proved PfP mentioned in Sect 
 4
4 above 
 Condition ( D2 ) seems clear by the definition of the predicate Pf , although all details of the workings of this predicate must be proved using low-level inferences in the HF calculus 
 Condition ( D3 ) can be regarded as a version of the theorem Sigma fm imp thm ( “ true Σ sentences are theorems ” ) internalised as a theorem of the internal calculus 
 So while we avoid having to formalise the whole of G¨odel ’ s theorem within the calculus , we end up formalising a key part of it 
 Condition ( D3 ) is stated in a general form , but we only need one specific instance : ⊢ Pf ( pαq ) → Pf ( pPf ( pαq ) q ) 
 Despite a superficial resemblance , ( D3 ) does not follow from ( D1 ) , which holds by induction on the proof of ⊢ α 
 As Swierczkowski explains [ 32 , p
 23 ] , condition ( D3 ) is ´ not general enough to prove by induction 
 In the sequel , we generalise and prove it 
 6
1 Pseudo-Coding Condition ( D3 ) can be proved by induction on α if the assertion is generalised so that α can have free variables , say x1 , 
 
 
 , xn : ⊢ α ( x1 , 
 
 
 , xn ) → Pf ( pα ( x1 , 
 
 
 , xn ) q ) The syntactic constructions used in this formula have to be formalised , and the necessary transformations have to be justified within the HF calculus 
 As mentioned above ( Sect 
 5 ) , the boldface convention needs to be made rigorous 
 In particular , codings are always ground HF terms , and yet pα ( x1 , 
 
 
 , xn ) q has a functional dependence ( as an HF term ) on x1 , 
 
 
 , xn 
 The first step in this process is to generalise coding to allow

Introspector: INPUT:!@>Seeker:#53 s theoremproving technology 
 25 A simpler route to the theorem involves the Hilbert-Bernays derivability conditions [ 2 , p
 15 ] [ 9 , p
 73 ] 
 If ⊢ α , then ⊢ Pf ( pαq ) ( D1 ) If ⊢ Pf ( pα → βq ) and ⊢ Pf ( pαq ) , then ⊢ Pf ( pβq ) ( D2 ) If α is a strict Σ sentence , then ⊢ α → Pf ( pαq ) ( D3 ) ( Where there is no ambiguity , we identify Pf with the formalised predicate PfP ; the latter is the actual HF predicate , but the notation Pf is widely used in the literature , along with G¨odel ’ s original Bew 
 ) Condition ( D1 ) is none other than the theorem proved iff proved PfP mentioned in Sect 
 4
4 above 
 Condition ( D2 ) seems clear by the definition of the predicate Pf , although all details of the workings of this predicate must be proved using low-level inferences in the HF calculus 
 Condition ( D3 ) can be regarded as a version of the theorem Sigma fm imp thm ( “ true Σ sentences are theorems ” ) internalised as a theorem of the internal calculus 
 So while we avoid having to formalise the whole of G¨odel ’ s theorem within the calculus , we end up formalising a key part of it 
 Condition ( D3 ) is stated in a general form , but we only need one specific instance : ⊢ Pf ( pαq ) → Pf ( pPf ( pαq ) q ) 
 Despite a superficial resemblance , ( D3 ) does not follow from ( D1 ) , which holds by induction on the proof of ⊢ α 
 As Swierczkowski explains [ 32 , p
 23 ] , condition ( D3 ) is ´ not general enough to prove by induction 
 In the sequel , we generalise and prove it 
 6
1 Pseudo-Coding Condition ( D3 ) can be proved by induction on α if the assertion is generalised so that α can have free variables , say x1 , 
 
 
 , xn : ⊢ α ( x1 , 
 
 
 , xn ) → Pf ( pα ( x1 , 
 
 
 , xn ) q ) The syntactic constructions used in this formula have to be formalised , and the necessary transformations have to be justified within the HF calculus 
 As mentioned above ( Sect 
 5 ) , the boldface convention needs to be made rigorous 
 In particular , codings are always ground HF terms , and yet pα ( x1 , 
 
 
 , xn ) q has a functional dependence ( as an HF term ) on x1 , 
 
 
 , xn 
 The first step in this process is to generalise coding to allow


free variables for α . This will require some care because the notion of a free variable depends on whether or not the context contains any quantifiers 
We begin by considering what happens when α includes at least one bound variable Xi such that Xi occurs freely in α 
For example consider the sentence  ¬p(x) ∧ p(y) ∧ y = x ∧ z = x where Z is another distinct name occurring freely in α 
Then clearly Y cannot occur anywhere inside the scope of any quantifier in α 
Next suppose that α were expanded into its normal form according to the rules of the HF grammar 
Then α would contain at most one occurrence of each constant symbol Cj and at most one occurrence of each relation Rij 
However since α contains at least two distinct names Xi and Zi both occurring freely in α , neither of these symbols could possibly represent any constant symbol Cj or relation Rij 
Therefore we conclude that whenever α contains at least one bound variable Xi whose value range overlaps with the domain of discourse of α itself , then Xi cannot appear inside the scope of any quantifier in α 
Now let us turn our attention to proving pseudo-coding condition (D3). To do this we introduce a new notion called the "codable" fragment of the language L. Specifically, given a set L of formulas, we define the codable fragment FL of L to consist of those formulas φ that can be obtained from L by replacing every occurrence of a bound variable Xi with either a constant symbol Ci or a relation Ri. More formally, FL consists of the following formulas: φ ::= pXi ∨ ¬pXi | pRi(Xa, Xb) ∨ ¬pRi(Xa, Xb) where Xa, Xb are fresh constants and i ranges over {1, ..., n}. Note that FL may include formulas containing free variables, even though they are not necessarily present in the input formula α. Our goal now is to show how to use pseudo-coding condition (D3) to establish the soundness of the system. Towards this end, we observe that pseudo-coding condition (D3) implies that if α is a valid formula in the codable fragment FL, then there exists a coding c such that α ⟦ c ⟧. Moreover, wefree variables for α . This will require some care because the notion of a free variable depends on whether or not the context contains any quantifiers 
We begin by considering what happens when α includes at least one bound variable Xi such that Xi occurs freely in α 
For example consider the sentence  ¬p(x) ∧ p(y) ∧ y = x ∧ z = x where Z is another distinct name occurring freely in α 
Then clearly Y cannot occur anywhere inside the scope of any quantifier in α 
Next suppose that α were expanded into its normal form according to the rules of the HF grammar 
Then α would contain at most one occurrence of each constant symbol Cj and at most one occurrence of each relation Rij 
However since α contains at least two distinct names Xi and Zi both occurring freely in α , neither of these symbols could possibly represent any constant symbol Cj or relation Rij 
Therefore we conclude that whenever α contains at least one bound variable Xi whose value range overlaps with the domain of discourse of α itself , then Xi cannot appear inside the scope of any quantifier in α 
Now let us turn our attention to proving pseudo-coding condition (D3). To do this we introduce a new notion called the "codable" fragment of the language L. Specifically, given a set L of formulas, we define the codable fragment FL of L to consist of those formulas φ that can be obtained from L by replacing every occurrence of a bound variable Xi with either a constant symbol Ci or a relation Ri. More formally, FL consists of the following formulas: φ ::= pXi ∨ ¬pXi | pRi(Xa, Xb) ∨ ¬pRi(Xa, Xb) where Xa, Xb are fresh constants and i ranges over {1, ..., n}. Note that FL may include formulas containing free variables, even though they are not necessarily present in the input formula α. Our goal now is to show how to use pseudo-coding condition (D3) to establish the soundness of the system. Towards this end, we observe that pseudo-coding condition (D3) implies that if α is a valid formula in the codable fragment FL, then there exists a coding c such that α ⟦ c ⟧. Moreover,


You: !@>Seeker:#54 induction on the proof of ⊢ α 
 As Swierczkowski explains [ 32 , p
 23 ] , condition ( D3 ) is ´ not general enough to prove by induction 
 In the sequel , we generalise and prove it 
 6
1 Pseudo-Coding Condition ( D3 ) can be proved by induction on α if the assertion is generalised so that α can have free variables , say x1 , 
 
 
 , xn : ⊢ α ( x1 , 
 
 
 , xn ) → Pf ( pα ( x1 , 
 
 
 , xn ) q ) The syntactic constructions used in this formula have to be formalised , and the necessary transformations have to be justified within the HF calculus 
 As mentioned above ( Sect 
 5 ) , the boldface convention needs to be made rigorous 
 In particular , codings are always ground HF terms , and yet pα ( x1 , 
 
 
 , xn ) q has a functional dependence ( as an HF term ) on x1 , 
 
 
 , xn 
 The first step in this process is to generalise coding to allow certain variables to be preserved as variables in the coded term 
 Recall that with normal quotations , every occurrence of a variable is replaced by the code of the variable name , ultimately a positive integer:7 function quot dbtm : : `` dbtm ⇒ tm '' where '' quot dbtm DBZero = Zero '' | `` quot dbtm ( DBVar name ) = ORD OF ( Suc ( nat of name name ) ) '' | 


 Now let us define the V -code of a term or formula , where V is a set of variables to be preserved in the code : 7 ORD OF ( Suc n ) denotes an HF term that denotes a positive integer , even if n is a variable 
 26 function vquot dbtm : : `` name set ⇒ dbtm ⇒ tm '' where '' vquot dbtm V DBZero = Zero '' | `` vquot dbtm V ( DBVar name ) = ( if name ∈ V then Var name else ORD OF ( Suc ( nat of name name ) ) ) '' | 


 V -coding is otherwise identical to standard coding , with the overloaded syntax ⌊A⌋V 
 The parameter V is necessary because not all variables should be preserved ; it will be necessary to consider a series of V -codes for V = ∅ , { x1 } 
 
 
 , { x1 , 
 
 
 , xn } 
 6
2 Simultaneous Substitution In order to formalise the notation pα ( x1 , 
 
 
 , xn ) q , it is convenient to introduce a function for simultaneous substitution 
 Here Swierczkowski ’ s presentation is a little ´ hard to follow : Suppose β is a theorem , i
e
 ,

Introspector: INPUT:!@>Seeker:#54 induction on the proof of ⊢ α 
 As Swierczkowski explains [ 32 , p
 23 ] , condition ( D3 ) is ´ not general enough to prove by induction 
 In the sequel , we generalise and prove it 
 6
1 Pseudo-Coding Condition ( D3 ) can be proved by induction on α if the assertion is generalised so that α can have free variables , say x1 , 
 
 
 , xn : ⊢ α ( x1 , 
 
 
 , xn ) → Pf ( pα ( x1 , 
 
 
 , xn ) q ) The syntactic constructions used in this formula have to be formalised , and the necessary transformations have to be justified within the HF calculus 
 As mentioned above ( Sect 
 5 ) , the boldface convention needs to be made rigorous 
 In particular , codings are always ground HF terms , and yet pα ( x1 , 
 
 
 , xn ) q has a functional dependence ( as an HF term ) on x1 , 
 
 
 , xn 
 The first step in this process is to generalise coding to allow certain variables to be preserved as variables in the coded term 
 Recall that with normal quotations , every occurrence of a variable is replaced by the code of the variable name , ultimately a positive integer:7 function quot dbtm : : `` dbtm ⇒ tm '' where '' quot dbtm DBZero = Zero '' | `` quot dbtm ( DBVar name ) = ORD OF ( Suc ( nat of name name ) ) '' | 


 Now let us define the V -code of a term or formula , where V is a set of variables to be preserved in the code : 7 ORD OF ( Suc n ) denotes an HF term that denotes a positive integer , even if n is a variable 
 26 function vquot dbtm : : `` name set ⇒ dbtm ⇒ tm '' where '' vquot dbtm V DBZero = Zero '' | `` vquot dbtm V ( DBVar name ) = ( if name ∈ V then Var name else ORD OF ( Suc ( nat of name name ) ) ) '' | 


 V -coding is otherwise identical to standard coding , with the overloaded syntax ⌊A⌋V 
 The parameter V is necessary because not all variables should be preserved ; it will be necessary to consider a series of V -codes for V = ∅ , { x1 } 
 
 
 , { x1 , 
 
 
 , xn } 
 6
2 Simultaneous Substitution In order to formalise the notation pα ( x1 , 
 
 
 , xn ) q , it is convenient to introduce a function for simultaneous substitution 
 Here Swierczkowski ’ s presentation is a little ´ hard to follow : Suppose β is a theorem , i
e
 ,




































































































































































































































































































































































































































































































































You: !@>Seeker:#55 preserved in the code : 7 ORD OF ( Suc n ) denotes an HF term that denotes a positive integer , even if n is a variable 
 26 function vquot dbtm : : `` name set ⇒ dbtm ⇒ tm '' where '' vquot dbtm V DBZero = Zero '' | `` vquot dbtm V ( DBVar name ) = ( if name ∈ V then Var name else ORD OF ( Suc ( nat of name name ) ) ) '' | 


 V -coding is otherwise identical to standard coding , with the overloaded syntax ⌊A⌋V 
 The parameter V is necessary because not all variables should be preserved ; it will be necessary to consider a series of V -codes for V = ∅ , { x1 } 
 
 
 , { x1 , 
 
 
 , xn } 
 6
2 Simultaneous Substitution In order to formalise the notation pα ( x1 , 
 
 
 , xn ) q , it is convenient to introduce a function for simultaneous substitution 
 Here Swierczkowski ’ s presentation is a little ´ hard to follow : Suppose β is a theorem , i
e
 , ⊢ β 
 If we replace each of the variables at each of its free occurrences in β by some constant term then the formula so obtained is also a theorem ( by the Substitution Rule 
 
 
 ) 
 This just described situation in the meta-theory admits description in HF 
 [ 32 , p
 24 ] It took me weeks of failed attempts to grasp the meaning of the phrase “ constant term ” 
 It does not mean a term containing no variables , but a term satisfying the predicate ConstP and thus denoting the code of a constant 
 Formalising this process seems to require replacing each variable xi by a new variable , x ′ i , intended to denote xi 
 Later , it will be constrained to do so by a suitable HF predicate 
 And so we need a function to perform simultaneous substitutions in a term for all variables in a set V 
 Using a “ fold ” operator over finite sets [ 19 ] eliminates the need to consider the variables in any particular order 
 definition ssubst : : `` tm ⇒ name set ⇒ ( name ⇒ tm ) ⇒ tm '' where `` ssubst t V F = Finite Set
fold ( λi 
 subst i ( F i ) ) t V '' The renaming of xi to x ′ i could be done using arithmetic on variable subscripts , but the formalisation instead follows an abstract approach , using nominal primitives 
 An Isabelle locale defines a proof context containing a permutation p ( mapping all variable names to new ones ) , a finite set Vs of variable names and finally the actual renaming function F , which simply applies the permutation to

Introspector: INPUT:!@>Seeker:#55 preserved in the code : 7 ORD OF ( Suc n ) denotes an HF term that denotes a positive integer , even if n is a variable 
 26 function vquot dbtm : : `` name set ⇒ dbtm ⇒ tm '' where '' vquot dbtm V DBZero = Zero '' | `` vquot dbtm V ( DBVar name ) = ( if name ∈ V then Var name else ORD OF ( Suc ( nat of name name ) ) ) '' | 


 V -coding is otherwise identical to standard coding , with the overloaded syntax ⌊A⌋V 
 The parameter V is necessary because not all variables should be preserved ; it will be necessary to consider a series of V -codes for V = ∅ , { x1 } 
 
 
 , { x1 , 
 
 
 , xn } 
 6
2 Simultaneous Substitution In order to formalise the notation pα ( x1 , 
 
 
 , xn ) q , it is convenient to introduce a function for simultaneous substitution 
 Here Swierczkowski ’ s presentation is a little ´ hard to follow : Suppose β is a theorem , i
e
 , ⊢ β 
 If we replace each of the variables at each of its free occurrences in β by some constant term then the formula so obtained is also a theorem ( by the Substitution Rule 
 
 
 ) 
 This just described situation in the meta-theory admits description in HF 
 [ 32 , p
 24 ] It took me weeks of failed attempts to grasp the meaning of the phrase “ constant term ” 
 It does not mean a term containing no variables , but a term satisfying the predicate ConstP and thus denoting the code of a constant 
 Formalising this process seems to require replacing each variable xi by a new variable , x ′ i , intended to denote xi 
 Later , it will be constrained to do so by a suitable HF predicate 
 And so we need a function to perform simultaneous substitutions in a term for all variables in a set V 
 Using a “ fold ” operator over finite sets [ 19 ] eliminates the need to consider the variables in any particular order 
 definition ssubst : : `` tm ⇒ name set ⇒ ( name ⇒ tm ) ⇒ tm '' where `` ssubst t V F = Finite Set
fold ( λi 
 subst i ( F i ) ) t V '' The renaming of xi to x ′ i could be done using arithmetic on variable subscripts , but the formalisation instead follows an abstract approach , using nominal primitives 
 An Isabelle locale defines a proof context containing a permutation p ( mapping all variable names to new ones ) , a finite set Vs of variable names and finally the actual renaming function F , which simply applies the permutation to


</s>


You: !@>Seeker:#56 of a constant 
 Formalising this process seems to require replacing each variable xi by a new variable , x ′ i , intended to denote xi 
 Later , it will be constrained to do so by a suitable HF predicate 
 And so we need a function to perform simultaneous substitutions in a term for all variables in a set V 
 Using a “ fold ” operator over finite sets [ 19 ] eliminates the need to consider the variables in any particular order 
 definition ssubst : : `` tm ⇒ name set ⇒ ( name ⇒ tm ) ⇒ tm '' where `` ssubst t V F = Finite Set
fold ( λi 
 subst i ( F i ) ) t V '' The renaming of xi to x ′ i could be done using arithmetic on variable subscripts , but the formalisation instead follows an abstract approach , using nominal primitives 
 An Isabelle locale defines a proof context containing a permutation p ( mapping all variable names to new ones ) , a finite set Vs of variable names and finally the actual renaming function F , which simply applies the permutation to any variable in Vs
 8 locale quote perm = fixes p : : perm and Vs : : `` name set '' and F : : `` name ⇒ tm '' assumes p : `` atom ‘ ( p · Vs ) ♯ * Vs '' and pinv : `` -p = p '' and Vs : `` finite Vs '' defines `` F ≡ make F Vs p '' Most proofs about ssubst are done within the context of this locale , because it provides sufficient conditions for the simultaneous substitution to be meaningful 
 The first condition states that p maps all the variables in Vs to variables outside of that set , while second condition states that p is its own inverse 
 This abstract approach is a little unwieldy at times , but its benefits can be seen in the simple fact below , which states the effect of the simultaneous substitution on a single variable 
 8 make F Vs p i = Var ( p · i ) provided i ∈ Vs
 27 lemma ssubst Var if : assumes `` finite V '' shows `` ssubst ( Var i ) V F = ( if i ∈ V then F i else Var i ) '' We need to show that the variables in the set Vs can be renamed , one at a time , in a pseudo-coded de Bruijn term 
 Let V ⊆ Vs and suppose that the variables in V have already been renamed , and choose one of the remaining variables , w
 It will be replaced by a new variable , computed by F w
 And something very subtle is happening : the variable w is represented in the term by its code , ⌈Var w⌉ 
 Its

Introspector: INPUT:!@>Seeker:#56 of a constant 
 Formalising this process seems to require replacing each variable xi by a new variable , x ′ i , intended to denote xi 
 Later , it will be constrained to do so by a suitable HF predicate 
 And so we need a function to perform simultaneous substitutions in a term for all variables in a set V 
 Using a “ fold ” operator over finite sets [ 19 ] eliminates the need to consider the variables in any particular order 
 definition ssubst : : `` tm ⇒ name set ⇒ ( name ⇒ tm ) ⇒ tm '' where `` ssubst t V F = Finite Set
fold ( λi 
 subst i ( F i ) ) t V '' The renaming of xi to x ′ i could be done using arithmetic on variable subscripts , but the formalisation instead follows an abstract approach , using nominal primitives 
 An Isabelle locale defines a proof context containing a permutation p ( mapping all variable names to new ones ) , a finite set Vs of variable names and finally the actual renaming function F , which simply applies the permutation to any variable in Vs
 8 locale quote perm = fixes p : : perm and Vs : : `` name set '' and F : : `` name ⇒ tm '' assumes p : `` atom ‘ ( p · Vs ) ♯ * Vs '' and pinv : `` -p = p '' and Vs : `` finite Vs '' defines `` F ≡ make F Vs p '' Most proofs about ssubst are done within the context of this locale , because it provides sufficient conditions for the simultaneous substitution to be meaningful 
 The first condition states that p maps all the variables in Vs to variables outside of that set , while second condition states that p is its own inverse 
 This abstract approach is a little unwieldy at times , but its benefits can be seen in the simple fact below , which states the effect of the simultaneous substitution on a single variable 
 8 make F Vs p i = Var ( p · i ) provided i ∈ Vs
 27 lemma ssubst Var if : assumes `` finite V '' shows `` ssubst ( Var i ) V F = ( if i ∈ V then F i else Var i ) '' We need to show that the variables in the set Vs can be renamed , one at a time , in a pseudo-coded de Bruijn term 
 Let V ⊆ Vs and suppose that the variables in V have already been renamed , and choose one of the remaining variables , w
 It will be replaced by a new variable , computed by F w
 And something very subtle is happening : the variable w is represented in the term by its code , ⌈Var w⌉ 
 Its

value depends only on the values of other variables in Vs , not just those assigned by F 
So when we substitute into the original term , the variable w has taken on a completely different meaning than before .
In some sense , what happens here is similar to how a computer program might use dynamic recompilation or reflection to change its behavior based on runtime data  
But unlike such programs , there's no real computational step involved – rather , the notion of substitution itself gets generalized from a sequential operation to a parallel one 
The key insight behind this generalization is that once you know enough information about the structure of your terms , including their dependencies between variables , you don’t actually _need_ to unroll them fully in order to reason about them 
Instead , you can focus directly on the relevant parts of the term without worrying too much about irrelevant details 
This allows us to develop more flexible and expressive mathematical structures , since we can now define functions that take arbitrary terms as input and produce equivalent output given certain constraints 
For example , we may want to define a function that takes two terms representing distinct objects and produces another term denoting their composition 
Or perhaps we wish to specify a family of functions parameterized by a natural number n , taking a term T(n) as input and producing a sequence of n identical copies of T applied repeatedly until stopping 
These kinds of abstraction allow us to build up complex systems out of simpler pieces , creating powerful tools for reasoning about mathematics and programming alike </s>value depends only on the values of other variables in Vs , not just those assigned by F 
So when we substitute into the original term , the variable w has taken on a completely different meaning than before .
In some sense , what happens here is similar to how a computer program might use dynamic recompilation or reflection to change its behavior based on runtime data  
But unlike such programs , there's no real computational step involved – rather , the notion of substitution itself gets generalized from a sequential operation to a parallel one 
The key insight behind this generalization is that once you know enough information about the structure of your terms , including their dependencies between variables , you don’t actually _need_ to unroll them fully in order to reason about them 
Instead , you can focus directly on the relevant parts of the term without worrying too much about irrelevant details 
This allows us to develop more flexible and expressive mathematical structures , since we can now define functions that take arbitrary terms as input and produce equivalent output given certain constraints 
For example , we may want to define a function that takes two terms representing distinct objects and produces another term denoting their composition 
Or perhaps we wish to specify a family of functions parameterized by a natural number n , taking a term T(n) as input and producing a sequence of n identical copies of T applied repeatedly until stopping 
These kinds of abstraction allow us to build up complex systems out of simpler pieces , creating powerful tools for reasoning about mathematics and programming alike


You: !@>Seeker:#57 that p maps all the variables in Vs to variables outside of that set , while second condition states that p is its own inverse 
 This abstract approach is a little unwieldy at times , but its benefits can be seen in the simple fact below , which states the effect of the simultaneous substitution on a single variable 
 8 make F Vs p i = Var ( p · i ) provided i ∈ Vs
 27 lemma ssubst Var if : assumes `` finite V '' shows `` ssubst ( Var i ) V F = ( if i ∈ V then F i else Var i ) '' We need to show that the variables in the set Vs can be renamed , one at a time , in a pseudo-coded de Bruijn term 
 Let V ⊆ Vs and suppose that the variables in V have already been renamed , and choose one of the remaining variables , w
 It will be replaced by a new variable , computed by F w
 And something very subtle is happening : the variable w is represented in the term by its code , ⌈Var w⌉ 
 Its replacement , F w , is Var ( p · w ) and a variable 
 lemma SubstTermP vquot dbtm : assumes w : `` w ∈ Vs - V '' and V : `` V ⊆ Vs '' `` V ’ = p · V '' and s : `` supp dbtm ⊆ atom ‘ Vs '' shows '' insert ( ConstP ( F w ) ) { ConstP ( F i ) | i
 i ∈ V } ⊢ SubstTermP ⌈Var w⌉ ( F w ) ( ssubst ( vquot dbtm V dbtm ) V F ) ( subst w ( F w ) ( ssubst ( vquot dbtm ( insert w V ) dbtm ) V F ) ) '' This theorem is proved by structural induction on dbtm , the de Bruijn term 
 The condition supp dbtm ⊆ atom ‘ Vs states that the free variables of dbtm all belong to Vs 
 The variable case of the induction is tricky ( and is the crux of the entire proof ) 
 We are working with a coded term that contains both coded variables and real ones ( of the form F i ) ; it is necessary to show that the real variables are preserved by the substitution , because they are the xi that we are trying to introduce 
 The F i are preserved under the assumption that they denote constants , which is the point of including the formulas ConstP ( F i ) for all i ∈ V on the left side of the turnstile 
 These assumptions will have to be justified later 
 Under virtually the same assumptions ( omitted ) , the analogous result holds for pseudo-coded de Bruijn formulas 
 lemma SubstFormP vquot dbfm : ''

Introspector: INPUT:!@>Seeker:#57 that p maps all the variables in Vs to variables outside of that set , while second condition states that p is its own inverse 
 This abstract approach is a little unwieldy at times , but its benefits can be seen in the simple fact below , which states the effect of the simultaneous substitution on a single variable 
 8 make F Vs p i = Var ( p · i ) provided i ∈ Vs
 27 lemma ssubst Var if : assumes `` finite V '' shows `` ssubst ( Var i ) V F = ( if i ∈ V then F i else Var i ) '' We need to show that the variables in the set Vs can be renamed , one at a time , in a pseudo-coded de Bruijn term 
 Let V ⊆ Vs and suppose that the variables in V have already been renamed , and choose one of the remaining variables , w
 It will be replaced by a new variable , computed by F w
 And something very subtle is happening : the variable w is represented in the term by its code , ⌈Var w⌉ 
 Its replacement , F w , is Var ( p · w ) and a variable 
 lemma SubstTermP vquot dbtm : assumes w : `` w ∈ Vs - V '' and V : `` V ⊆ Vs '' `` V ’ = p · V '' and s : `` supp dbtm ⊆ atom ‘ Vs '' shows '' insert ( ConstP ( F w ) ) { ConstP ( F i ) | i
 i ∈ V } ⊢ SubstTermP ⌈Var w⌉ ( F w ) ( ssubst ( vquot dbtm V dbtm ) V F ) ( subst w ( F w ) ( ssubst ( vquot dbtm ( insert w V ) dbtm ) V F ) ) '' This theorem is proved by structural induction on dbtm , the de Bruijn term 
 The condition supp dbtm ⊆ atom ‘ Vs states that the free variables of dbtm all belong to Vs 
 The variable case of the induction is tricky ( and is the crux of the entire proof ) 
 We are working with a coded term that contains both coded variables and real ones ( of the form F i ) ; it is necessary to show that the real variables are preserved by the substitution , because they are the xi that we are trying to introduce 
 The F i are preserved under the assumption that they denote constants , which is the point of including the formulas ConstP ( F i ) for all i ∈ V on the left side of the turnstile 
 These assumptions will have to be justified later 
 Under virtually the same assumptions ( omitted ) , the analogous result holds for pseudo-coded de Bruijn formulas 
 lemma SubstFormP vquot dbfm : ''

assuming w : “w ∈ Vs –V” and V : "V ⊆ Vs" and showing “insert (ConstP(Fw)){ConstP(Fi)|i ∈ V} ⊢SubstFormP⌈Var w⌉(Fw)(ssubst(v quot dbfm V dbfm)V F)}”
This theorem follows from the previous one by applying the Yoneda embedding functor to the first instance .
The key insight here is that the notion of renaming used in these lemmas is not quite the standard notion of renaming found in category theory or programming languages; rather than simply replacing each occurrence of an old name with a new name, we must carefully track how many occurrences there were of each name before the rename occurred.”</s>assuming w : “w ∈ Vs –V” and V : "V ⊆ Vs" and showing “insert (ConstP(Fw)){ConstP(Fi)|i ∈ V} ⊢SubstFormP⌈Var w⌉(Fw)(ssubst(v quot dbfm V dbfm)V F)}”
This theorem follows from the previous one by applying the Yoneda embedding functor to the first instance .
The key insight here is that the notion of renaming used in these lemmas is not quite the standard notion of renaming found in category theory or programming languages; rather than simply replacing each occurrence of an old name with a new name, we must carefully track how many occurrences there were of each name before the rename


You: !@>Seeker:#58 subst w ( F w ) ( ssubst ( vquot dbtm ( insert w V ) dbtm ) V F ) ) '' This theorem is proved by structural induction on dbtm , the de Bruijn term 
 The condition supp dbtm ⊆ atom ‘ Vs states that the free variables of dbtm all belong to Vs 
 The variable case of the induction is tricky ( and is the crux of the entire proof ) 
 We are working with a coded term that contains both coded variables and real ones ( of the form F i ) ; it is necessary to show that the real variables are preserved by the substitution , because they are the xi that we are trying to introduce 
 The F i are preserved under the assumption that they denote constants , which is the point of including the formulas ConstP ( F i ) for all i ∈ V on the left side of the turnstile 
 These assumptions will have to be justified later 
 Under virtually the same assumptions ( omitted ) , the analogous result holds for pseudo-coded de Bruijn formulas 
 lemma SubstFormP vquot dbfm : '' insert ( ConstP ( F w ) ) { ConstP ( F i ) | i
 i ∈ V } ⊢ SubstFormP ⌈Var w⌉ ( F w ) ( ssubst ( vquot dbfm V dbfm ) V F ) ( subst w ( F w ) ( ssubst ( vquot dbfm ( insert w V ) dbfm ) V F ) ) '' The proof is an easy structural induction on dbfm 
 Every case holds immediately by properties of substitution and the induction hypotheses or by the previous theorem , for terms 
 The only difficult case in these two proofs is the variable case discussed above 
 Using the notation for V -coding , we can see that the substitution predicate SubstFormP can transform the term ssubst ⌊A⌋V V F into ssubst ⌊A⌋ ( insert w V ) ( insert w V ) F
 Repeating this step , we can replace any finite set of variables in a coded formula by real ones , realising Swierczkowski ’ s remark quoted at the top of this section , an ´ d in particular his last sentence 
 That is , if β is a theorem in HF ( if ⊢ Pf β holds ) then the result of substituting constants for its variables is also an HF theorem 
 More precisely still , we are replacing some subset V of the variables by fresh variables ( the F i ) , constrained by the predicate ConstP 
 theorem PfP implies PfP ssubst : fixes β : :fm assumes β : `` { } ⊢ PfP ⌈β⌉ '' and V : `` V ⊆ Vs '' and s : `` supp β ⊆ atom ‘ Vs '' shows `` { ConstP ( F i ) | i
 i ∈ V

Introspector: INPUT:!@>Seeker:#58 subst w ( F w ) ( ssubst ( vquot dbtm ( insert w V ) dbtm ) V F ) ) '' This theorem is proved by structural induction on dbtm , the de Bruijn term 
 The condition supp dbtm ⊆ atom ‘ Vs states that the free variables of dbtm all belong to Vs 
 The variable case of the induction is tricky ( and is the crux of the entire proof ) 
 We are working with a coded term that contains both coded variables and real ones ( of the form F i ) ; it is necessary to show that the real variables are preserved by the substitution , because they are the xi that we are trying to introduce 
 The F i are preserved under the assumption that they denote constants , which is the point of including the formulas ConstP ( F i ) for all i ∈ V on the left side of the turnstile 
 These assumptions will have to be justified later 
 Under virtually the same assumptions ( omitted ) , the analogous result holds for pseudo-coded de Bruijn formulas 
 lemma SubstFormP vquot dbfm : '' insert ( ConstP ( F w ) ) { ConstP ( F i ) | i
 i ∈ V } ⊢ SubstFormP ⌈Var w⌉ ( F w ) ( ssubst ( vquot dbfm V dbfm ) V F ) ( subst w ( F w ) ( ssubst ( vquot dbfm ( insert w V ) dbfm ) V F ) ) '' The proof is an easy structural induction on dbfm 
 Every case holds immediately by properties of substitution and the induction hypotheses or by the previous theorem , for terms 
 The only difficult case in these two proofs is the variable case discussed above 
 Using the notation for V -coding , we can see that the substitution predicate SubstFormP can transform the term ssubst ⌊A⌋V V F into ssubst ⌊A⌋ ( insert w V ) ( insert w V ) F
 Repeating this step , we can replace any finite set of variables in a coded formula by real ones , realising Swierczkowski ’ s remark quoted at the top of this section , an ´ d in particular his last sentence 
 That is , if β is a theorem in HF ( if ⊢ Pf β holds ) then the result of substituting constants for its variables is also an HF theorem 
 More precisely still , we are replacing some subset V of the variables by fresh variables ( the F i ) , constrained by the predicate ConstP 
 theorem PfP implies PfP ssubst : fixes β : :fm assumes β : `` { } ⊢ PfP ⌈β⌉ '' and V : `` V ⊆ Vs '' and s : `` supp β ⊆ atom ‘ Vs '' shows `` { ConstP ( F i ) | i
 i ∈ V

} ⊢ PfP ⌈SubstFormP β⌉ ''.''
The key insight here is that the substitution predicate SubstFormP preserves the structure of the original formula , while introducing new variables that may refer to arbitrary constant expressions . By repeating this process several times , we can reduce the problem of proving the soundness of a given formula to one of showing that certain subformulas hold within a restricted fragment of propositional logic .</s>} ⊢ PfP ⌈SubstFormP β⌉ ''.''
The key insight here is that the substitution predicate SubstFormP preserves the structure of the original formula , while introducing new variables that may refer to arbitrary constant expressions . By repeating this process several times , we can reduce the problem of proving the soundness of a given formula to one of showing that certain subformulas hold within a restricted fragment of propositional logic


You: !@>Seeker:#59 two proofs is the variable case discussed above 
 Using the notation for V -coding , we can see that the substitution predicate SubstFormP can transform the term ssubst ⌊A⌋V V F into ssubst ⌊A⌋ ( insert w V ) ( insert w V ) F
 Repeating this step , we can replace any finite set of variables in a coded formula by real ones , realising Swierczkowski ’ s remark quoted at the top of this section , an ´ d in particular his last sentence 
 That is , if β is a theorem in HF ( if ⊢ Pf β holds ) then the result of substituting constants for its variables is also an HF theorem 
 More precisely still , we are replacing some subset V of the variables by fresh variables ( the F i ) , constrained by the predicate ConstP 
 theorem PfP implies PfP ssubst : fixes β : :fm assumes β : `` { } ⊢ PfP ⌈β⌉ '' and V : `` V ⊆ Vs '' and s : `` supp β ⊆ atom ‘ Vs '' shows `` { ConstP ( F i ) | i
 i ∈ V } ⊢ PfP ( ssubst ⌊β⌋V V F ) '' 28 The effort needed to formalise the results outlined above is relatively modest , at 330 lines of Isabelle/HOL , but this excludes the effort needed to prove some essential lemmas , which state that the various syntactic predicates work correctly 
 Because these proofs concern non-ground HF formulas , theorem Sigma fm imp thm does not help 
 Required is an HF formalisation of operations on sequences , such as concatenation 
 That in turn requires formalising further operations such as addition and set union 
 These proofs ( which are conducted largely in the HF calculus ) total over 2,800 lines 
 This total includes a library of results for truncating and concatenating sequences 
 Here is a selection of the results proved 
 Substitution preserves the value Zero : theorem SubstTermP Zero : `` { TermP t } ⊢ SubstTermP ⌈Var v⌉ t Zero Zero '' On terms constructed using Eats ( recall that Q Eats constructs the code of an Eats term ) , substitution performs the natural recursion 
 theorem SubstTermP Eats : '' { SubstTermP v i t1 u1 , SubstTermP v i t2 u2 } ⊢ SubstTermP v i ( Q Eats t1 t2 ) ( Q Eats u1 u2 ) '' This seemingly obvious result takes nearly 150 lines to prove 
 The sequences for both substitution computations are combined to form a new sequence , which must be extended to yield the claimed result and shown to be properly constructed 
 Substitution preserves constants 
 This fact is proved by induction on the sequence buildup of the constant c , using the previous two facts about SubstTermP 
 theorem SubstTermP Const : `` { ConstP c , TermP t } ⊢

Introspector: INPUT:!@>Seeker:#59 two proofs is the variable case discussed above 
 Using the notation for V -coding , we can see that the substitution predicate SubstFormP can transform the term ssubst ⌊A⌋V V F into ssubst ⌊A⌋ ( insert w V ) ( insert w V ) F
 Repeating this step , we can replace any finite set of variables in a coded formula by real ones , realising Swierczkowski ’ s remark quoted at the top of this section , an ´ d in particular his last sentence 
 That is , if β is a theorem in HF ( if ⊢ Pf β holds ) then the result of substituting constants for its variables is also an HF theorem 
 More precisely still , we are replacing some subset V of the variables by fresh variables ( the F i ) , constrained by the predicate ConstP 
 theorem PfP implies PfP ssubst : fixes β : :fm assumes β : `` { } ⊢ PfP ⌈β⌉ '' and V : `` V ⊆ Vs '' and s : `` supp β ⊆ atom ‘ Vs '' shows `` { ConstP ( F i ) | i
 i ∈ V } ⊢ PfP ( ssubst ⌊β⌋V V F ) '' 28 The effort needed to formalise the results outlined above is relatively modest , at 330 lines of Isabelle/HOL , but this excludes the effort needed to prove some essential lemmas , which state that the various syntactic predicates work correctly 
 Because these proofs concern non-ground HF formulas , theorem Sigma fm imp thm does not help 
 Required is an HF formalisation of operations on sequences , such as concatenation 
 That in turn requires formalising further operations such as addition and set union 
 These proofs ( which are conducted largely in the HF calculus ) total over 2,800 lines 
 This total includes a library of results for truncating and concatenating sequences 
 Here is a selection of the results proved 
 Substitution preserves the value Zero : theorem SubstTermP Zero : `` { TermP t } ⊢ SubstTermP ⌈Var v⌉ t Zero Zero '' On terms constructed using Eats ( recall that Q Eats constructs the code of an Eats term ) , substitution performs the natural recursion 
 theorem SubstTermP Eats : '' { SubstTermP v i t1 u1 , SubstTermP v i t2 u2 } ⊢ SubstTermP v i ( Q Eats t1 t2 ) ( Q Eats u1 u2 ) '' This seemingly obvious result takes nearly 150 lines to prove 
 The sequences for both substitution computations are combined to form a new sequence , which must be extended to yield the claimed result and shown to be properly constructed 
 Substitution preserves constants 
 This fact is proved by induction on the sequence buildup of the constant c , using the previous two facts about SubstTermP 
 theorem SubstTermP Const : `` { ConstP c , TermP t } ⊢

SubstTermP c ( Var x y z ) t = c ( Var x y z ) t ''.
This proof consists of showing that each subterm of the original expression has been replaced by one or more equivalent expressions involving only the free variables .
The first part of the proof uses the definition of SubstTermP to show how the outermost occurrence of `Const' may be eliminated through repeated application of SubstTermP 
Next comes the hard bit – proving that every instance of `Const’ within the remaining subterms will have been transformed into an expression containing no occurrences of `Const', via another series of applications of SubstTermP.
Finally, it remains to check that all instances of `Const' outside the scope of any occurrence of `Var' have indeed become Constant terms themselves!
In summary, the key insight here is that substitution works equally well whether applied directly to atomic terms or to complex constructions built up from simpler pieces; thus, once we know what happens when applying substitution to simple atoms, we simply need to repeat those same steps many times until reaching our goal term...”</s>SubstTermP c ( Var x y z ) t = c ( Var x y z ) t ''.
This proof consists of showing that each subterm of the original expression has been replaced by one or more equivalent expressions involving only the free variables .
The first part of the proof uses the definition of SubstTermP to show how the outermost occurrence of `Const' may be eliminated through repeated application of SubstTermP 
Next comes the hard bit – proving that every instance of `Const’ within the remaining subterms will have been transformed into an expression containing no occurrences of `Const', via another series of applications of SubstTermP.
Finally, it remains to check that all instances of `Const' outside the scope of any occurrence of `Var' have indeed become Constant terms themselves!
In summary, the key insight here is that substitution works equally well whether applied directly to atomic terms or to complex constructions built up from simpler pieces; thus, once we know what happens when applying substitution to simple atoms, we simply need to repeat those same steps many times until reaching our goal


You: !@>Seeker:#60 which are conducted largely in the HF calculus ) total over 2,800 lines 
 This total includes a library of results for truncating and concatenating sequences 
 Here is a selection of the results proved 
 Substitution preserves the value Zero : theorem SubstTermP Zero : `` { TermP t } ⊢ SubstTermP ⌈Var v⌉ t Zero Zero '' On terms constructed using Eats ( recall that Q Eats constructs the code of an Eats term ) , substitution performs the natural recursion 
 theorem SubstTermP Eats : '' { SubstTermP v i t1 u1 , SubstTermP v i t2 u2 } ⊢ SubstTermP v i ( Q Eats t1 t2 ) ( Q Eats u1 u2 ) '' This seemingly obvious result takes nearly 150 lines to prove 
 The sequences for both substitution computations are combined to form a new sequence , which must be extended to yield the claimed result and shown to be properly constructed 
 Substitution preserves constants 
 This fact is proved by induction on the sequence buildup of the constant c , using the previous two facts about SubstTermP 
 theorem SubstTermP Const : `` { ConstP c , TermP t } ⊢ SubstTermP ⌈Var w⌉ t c c '' Each recursive case of a syntactic predicate must be verified using the techniques outlined above for SubstTermP Eats 
 Even when there is only a single operand , as in the following case for negation , the proof is around 100 lines 
 theorem SubstFormP Neg : `` { SubstFormP v i x y } ⊢ SubstFormP v i ( Q Neg x ) ( Q Neg y ) '' A complication is that LstSeqP accepts sequences that are longer than necessary , and these must be truncated to a given length before they can be extended 
 These lengthy arguments must be repeated for each similar proof 
 So , for the third time , one of our chief tools is cut and paste 
 Exactly the same sort of reasoning can be used to show that proofs can be combined as expected in order to apply inference rules 
 The following theorem expresses the Hilbert-Bernays derivability condition ( D2 ) : theorem PfP implies ModPon PfP : `` [ [ H ⊢ PfP ( Q Imp x y ) ; H ⊢ PfP x ] ] =⇒ H ⊢ PfP y '' Now only one task remains : to show condition ( D3 ) 
 6
3 Making Sense of Quoted Values As mentioned in Sect 
 5 , making sense of expressions like x = y → Pf px = yq requires a function Q such that Q ( x ) = pxq : Q ( 0 ) = p0q = 0 Q ( x ⊳ y ) = hp⊳q , Q ( x ) , Q ( y ) i 29 Trying to make this definition unambiguous , Swierczkowski [ 32 ] sketches a total order- ´ ing on sets

Introspector: INPUT:!@>Seeker:#60 which are conducted largely in the HF calculus ) total over 2,800 lines 
 This total includes a library of results for truncating and concatenating sequences 
 Here is a selection of the results proved 
 Substitution preserves the value Zero : theorem SubstTermP Zero : `` { TermP t } ⊢ SubstTermP ⌈Var v⌉ t Zero Zero '' On terms constructed using Eats ( recall that Q Eats constructs the code of an Eats term ) , substitution performs the natural recursion 
 theorem SubstTermP Eats : '' { SubstTermP v i t1 u1 , SubstTermP v i t2 u2 } ⊢ SubstTermP v i ( Q Eats t1 t2 ) ( Q Eats u1 u2 ) '' This seemingly obvious result takes nearly 150 lines to prove 
 The sequences for both substitution computations are combined to form a new sequence , which must be extended to yield the claimed result and shown to be properly constructed 
 Substitution preserves constants 
 This fact is proved by induction on the sequence buildup of the constant c , using the previous two facts about SubstTermP 
 theorem SubstTermP Const : `` { ConstP c , TermP t } ⊢ SubstTermP ⌈Var w⌉ t c c '' Each recursive case of a syntactic predicate must be verified using the techniques outlined above for SubstTermP Eats 
 Even when there is only a single operand , as in the following case for negation , the proof is around 100 lines 
 theorem SubstFormP Neg : `` { SubstFormP v i x y } ⊢ SubstFormP v i ( Q Neg x ) ( Q Neg y ) '' A complication is that LstSeqP accepts sequences that are longer than necessary , and these must be truncated to a given length before they can be extended 
 These lengthy arguments must be repeated for each similar proof 
 So , for the third time , one of our chief tools is cut and paste 
 Exactly the same sort of reasoning can be used to show that proofs can be combined as expected in order to apply inference rules 
 The following theorem expresses the Hilbert-Bernays derivability condition ( D2 ) : theorem PfP implies ModPon PfP : `` [ [ H ⊢ PfP ( Q Imp x y ) ; H ⊢ PfP x ] ] =⇒ H ⊢ PfP y '' Now only one task remains : to show condition ( D3 ) 
 6
3 Making Sense of Quoted Values As mentioned in Sect 
 5 , making sense of expressions like x = y → Pf px = yq requires a function Q such that Q ( x ) = pxq : Q ( 0 ) = p0q = 0 Q ( x ⊳ y ) = hp⊳q , Q ( x ) , Q ( y ) i 29 Trying to make this definition unambiguous , Swierczkowski [ 32 ] sketches a total order- ´ ing on sets

In particular he shows how to define a notion of “equivalence” between any two elements of his set X 
But what does it mean if we have a pair of values q r such that Q ( x ) = qr ? We know from Definitions 4–7 that q cannot simply equal r because then we would not have anything interesting going on at all . Instead we need some way of saying that q has been transformed into something equivalent to r through application of the relevant functions F and G . One possible approach here might involve defining a notion of “conversion” or “transformation” between pairs of values—for example by introducing a notion of “homomorphism” between certain types of mathematical structures . However even if we could do so convincingly , I doubt whether anyone would find much use for such machinery outside of very specialized contexts where rigorous logical analysis is essential . For instance suppose we had found ways to transform every expression involving variables into its corresponding quotient expression without changing their meaning; this would clearly simplify many aspects of programming but hardly seems worth bothering about unless someone actually needs those simplifications badly enough to go to great lengths trying to achieve them!
In summary while definitional issues may arise whenever dealing directly with quoted values within formal systems themselves – especially regarding questions related either explicitly stated definitions contained therein OR more subtle matters concerning interpretation/application potentialities inherent various formsalisms employed throughout different domains – nevertheless overall experience suggests little practical utility accrues via pursuing detailed investigations aimed solely towards resolving said problems exclusively via means internal TO those respective frameworks alone…</s>In particular he shows how to define a notion of “equivalence” between any two elements of his set X 
But what does it mean if we have a pair of values q r such that Q ( x ) = qr ? We know from Definitions 4–7 that q cannot simply equal r because then we would not have anything interesting going on at all . Instead we need some way of saying that q has been transformed into something equivalent to r through application of the relevant functions F and G . One possible approach here might involve defining a notion of “conversion” or “transformation” between pairs of values—for example by introducing a notion of “homomorphism” between certain types of mathematical structures . However even if we could do so convincingly , I doubt whether anyone would find much use for such machinery outside of very specialized contexts where rigorous logical analysis is essential . For instance suppose we had found ways to transform every expression involving variables into its corresponding quotient expression without changing their meaning; this would clearly simplify many aspects of programming but hardly seems worth bothering about unless someone actually needs those simplifications badly enough to go to great lengths trying to achieve them!
In summary while definitional issues may arise whenever dealing directly with quoted values within formal systems themselves – especially regarding questions related either explicitly stated definitions contained therein OR more subtle matters concerning interpretation/application potentialities inherent various formsalisms employed throughout different domains – nevertheless overall experience suggests little practical utility accrues via pursuing detailed investigations aimed solely towards resolving said problems exclusively via means internal TO those respective frameworks


You: !@>Seeker:#61 they can be extended 
 These lengthy arguments must be repeated for each similar proof 
 So , for the third time , one of our chief tools is cut and paste 
 Exactly the same sort of reasoning can be used to show that proofs can be combined as expected in order to apply inference rules 
 The following theorem expresses the Hilbert-Bernays derivability condition ( D2 ) : theorem PfP implies ModPon PfP : `` [ [ H ⊢ PfP ( Q Imp x y ) ; H ⊢ PfP x ] ] =⇒ H ⊢ PfP y '' Now only one task remains : to show condition ( D3 ) 
 6
3 Making Sense of Quoted Values As mentioned in Sect 
 5 , making sense of expressions like x = y → Pf px = yq requires a function Q such that Q ( x ) = pxq : Q ( 0 ) = p0q = 0 Q ( x ⊳ y ) = hp⊳q , Q ( x ) , Q ( y ) i 29 Trying to make this definition unambiguous , Swierczkowski [ 32 ] sketches a total order- ´ ing on sets , but the technical details are complicated and incomplete 
 The same ordering can be defined via the function f : HF → N such that f ( x ) = P { 2 f ( y ) | y ∈ x } 
 It is intuitively clear , but formalising the required theory in HF would be laborious 
 It turns out that we do not need a canonical term x or a function Q 
 We only need a relation : QuoteP relates a set x to ( the codes of ) the terms that denote x 
 The relation QuoteP can be defined using precisely the same methods as we have seen above for recursive functions , via a sequence buildup 
 The following facts can be proved using the methods described in the previous sections 
 lemma QuoteP Zero : `` { } ⊢ QuoteP Zero Zero '' lemma QuoteP Eats : '' { QuoteP t1 u1 , QuoteP t2 u2 } ⊢ QuoteP ( Eats t1 t2 ) ( Q Eats u1 u2 ) '' It is also necessary to prove ( by induction within the HF calculus ) that for every x there exists some term x
 lemma exists QuoteP : assumes j : `` atom j ♯ x '' shows `` { } ⊢ Ex j ( QuoteP x ( Var j ) ) '' We need similar results for all of the predicates involved in concatenating two sequences 
 They essentially prove that the corresponding pseudo-functions are total 
 Now we need to start connecting these results with those of the previous section , which ( following Swierczkowski ) are proved for constants in general , althou ´ gh they are needed only for the outputs of QuoteP 
 An induction in

Introspector: INPUT:!@>Seeker:#61 they can be extended 
 These lengthy arguments must be repeated for each similar proof 
 So , for the third time , one of our chief tools is cut and paste 
 Exactly the same sort of reasoning can be used to show that proofs can be combined as expected in order to apply inference rules 
 The following theorem expresses the Hilbert-Bernays derivability condition ( D2 ) : theorem PfP implies ModPon PfP : `` [ [ H ⊢ PfP ( Q Imp x y ) ; H ⊢ PfP x ] ] =⇒ H ⊢ PfP y '' Now only one task remains : to show condition ( D3 ) 
 6
3 Making Sense of Quoted Values As mentioned in Sect 
 5 , making sense of expressions like x = y → Pf px = yq requires a function Q such that Q ( x ) = pxq : Q ( 0 ) = p0q = 0 Q ( x ⊳ y ) = hp⊳q , Q ( x ) , Q ( y ) i 29 Trying to make this definition unambiguous , Swierczkowski [ 32 ] sketches a total order- ´ ing on sets , but the technical details are complicated and incomplete 
 The same ordering can be defined via the function f : HF → N such that f ( x ) = P { 2 f ( y ) | y ∈ x } 
 It is intuitively clear , but formalising the required theory in HF would be laborious 
 It turns out that we do not need a canonical term x or a function Q 
 We only need a relation : QuoteP relates a set x to ( the codes of ) the terms that denote x 
 The relation QuoteP can be defined using precisely the same methods as we have seen above for recursive functions , via a sequence buildup 
 The following facts can be proved using the methods described in the previous sections 
 lemma QuoteP Zero : `` { } ⊢ QuoteP Zero Zero '' lemma QuoteP Eats : '' { QuoteP t1 u1 , QuoteP t2 u2 } ⊢ QuoteP ( Eats t1 t2 ) ( Q Eats u1 u2 ) '' It is also necessary to prove ( by induction within the HF calculus ) that for every x there exists some term x
 lemma exists QuoteP : assumes j : `` atom j ♯ x '' shows `` { } ⊢ Ex j ( QuoteP x ( Var j ) ) '' We need similar results for all of the predicates involved in concatenating two sequences 
 They essentially prove that the corresponding pseudo-functions are total 
 Now we need to start connecting these results with those of the previous section , which ( following Swierczkowski ) are proved for constants in general , althou ´ gh they are needed only for the outputs of QuoteP 
 An induction in

7 Conclusion  In conclusion , we have shown how to use the HF calculus to reason about quoted values . By defining a notion of quote and proving its properties through an adaptation of the standard techniques from category theory , we were able to establish connections between the original and quotient theories . This result provides evidence that the approach based on categorical semantics has potential applications beyond simply providing a foundation for programming languages .</s>7 Conclusion  In conclusion , we have shown how to use the HF calculus to reason about quoted values . By defining a notion of quote and proving its properties through an adaptation of the standard techniques from category theory , we were able to establish connections between the original and quotient theories . This result provides evidence that the approach based on categorical semantics has potential applications beyond simply providing a foundation for programming languages


You: !@>Seeker:#62 The relation QuoteP can be defined using precisely the same methods as we have seen above for recursive functions , via a sequence buildup 
 The following facts can be proved using the methods described in the previous sections 
 lemma QuoteP Zero : `` { } ⊢ QuoteP Zero Zero '' lemma QuoteP Eats : '' { QuoteP t1 u1 , QuoteP t2 u2 } ⊢ QuoteP ( Eats t1 t2 ) ( Q Eats u1 u2 ) '' It is also necessary to prove ( by induction within the HF calculus ) that for every x there exists some term x
 lemma exists QuoteP : assumes j : `` atom j ♯ x '' shows `` { } ⊢ Ex j ( QuoteP x ( Var j ) ) '' We need similar results for all of the predicates involved in concatenating two sequences 
 They essentially prove that the corresponding pseudo-functions are total 
 Now we need to start connecting these results with those of the previous section , which ( following Swierczkowski ) are proved for constants in general , althou ´ gh they are needed only for the outputs of QuoteP 
 An induction in HF on the sequence buildup proves that these outputs satisfy ConstP 
 lemma QuoteP imp ConstP : `` { QuoteP x y } ⊢ ConstP y '' This is obvious , because QuoteP involves only Zero and Q Eats , which construct quoted sets 
 Unfortunately , the proof requires the usual reasoning about sequences in order to show basic facts about ConstP , which takes hundreds of lines 
 The main theorem from the previous section included the set of formulas { ConstP ( F i ) | i
 i ∈ V } on the left of the turnstile , representing the assumption that all introduced variables denoted constants 
 Now we can replace this assumption by one expressing that the relation QuoteP holds between each pair of old and new variables 
 definition quote all : : `` [ perm , name set ] ⇒ fm set '' where `` quote all p V = { QuoteP ( Var i ) ( Var ( p · i ) ) | i
 i ∈ V } The relation QuoteP ( Var i ) ( Var ( p · i ) holds between the variable i and the renamed variable p · i , for all i ∈ V
 Recall that p is a permutation on variable names 
 By virtue of the theorem QuoteP imp ConstP , we obtain a key result , which will be used heavily in subsequent proofs for reasoning about coded formulas and the Pf predicate 
 theorem quote all PfP ssubst : assumes β : `` { } ⊢ β '' and V : `` V ⊆ Vs '' and s : `` supp β ⊆ atom ‘ Vs '' shows `` quote all p V ⊢ PfP ( ssubst ⌊β⌋V V F )

Introspector: INPUT:!@>Seeker:#62 The relation QuoteP can be defined using precisely the same methods as we have seen above for recursive functions , via a sequence buildup 
 The following facts can be proved using the methods described in the previous sections 
 lemma QuoteP Zero : `` { } ⊢ QuoteP Zero Zero '' lemma QuoteP Eats : '' { QuoteP t1 u1 , QuoteP t2 u2 } ⊢ QuoteP ( Eats t1 t2 ) ( Q Eats u1 u2 ) '' It is also necessary to prove ( by induction within the HF calculus ) that for every x there exists some term x
 lemma exists QuoteP : assumes j : `` atom j ♯ x '' shows `` { } ⊢ Ex j ( QuoteP x ( Var j ) ) '' We need similar results for all of the predicates involved in concatenating two sequences 
 They essentially prove that the corresponding pseudo-functions are total 
 Now we need to start connecting these results with those of the previous section , which ( following Swierczkowski ) are proved for constants in general , althou ´ gh they are needed only for the outputs of QuoteP 
 An induction in HF on the sequence buildup proves that these outputs satisfy ConstP 
 lemma QuoteP imp ConstP : `` { QuoteP x y } ⊢ ConstP y '' This is obvious , because QuoteP involves only Zero and Q Eats , which construct quoted sets 
 Unfortunately , the proof requires the usual reasoning about sequences in order to show basic facts about ConstP , which takes hundreds of lines 
 The main theorem from the previous section included the set of formulas { ConstP ( F i ) | i
 i ∈ V } on the left of the turnstile , representing the assumption that all introduced variables denoted constants 
 Now we can replace this assumption by one expressing that the relation QuoteP holds between each pair of old and new variables 
 definition quote all : : `` [ perm , name set ] ⇒ fm set '' where `` quote all p V = { QuoteP ( Var i ) ( Var ( p · i ) ) | i
 i ∈ V } The relation QuoteP ( Var i ) ( Var ( p · i ) holds between the variable i and the renamed variable p · i , for all i ∈ V
 Recall that p is a permutation on variable names 
 By virtue of the theorem QuoteP imp ConstP , we obtain a key result , which will be used heavily in subsequent proofs for reasoning about coded formulas and the Pf predicate 
 theorem quote all PfP ssubst : assumes β : `` { } ⊢ β '' and V : `` V ⊆ Vs '' and s : `` supp β ⊆ atom ‘ Vs '' shows `` quote all p V ⊢ PfP ( ssubst ⌊β⌋V V F )

In other words , given any formula β containing free occurrences of atoms from Vs , we may substitute into it any occurrence of an atom Aj from AtomsVs using the function ssubst ⌊β⌋V V F . The resulting formula still contains no free occurrences of atoms outside Vs 
Using this technique , we can easily reason about coded formulas without having to explicitly consider their structure or manipulate them directly 
Next step would be to define a notion of "coded" formulas more generally than just atomic ones - perhaps something like "formulae built up out of smaller pieces according to certain rules".
In summary , our goal here was to establish a connection between the relations studied previously and the current context of coded formulas and PfP . While doing so required us to introduce several novel notions such as "quoting", "renaming", etc., ultimately we were able to demonstrate how these relate back to familiar ideas from earlier work on relational semantics."</s>In other words , given any formula β containing free occurrences of atoms from Vs , we may substitute into it any occurrence of an atom Aj from AtomsVs using the function ssubst ⌊β⌋V V F . The resulting formula still contains no free occurrences of atoms outside Vs 
Using this technique , we can easily reason about coded formulas without having to explicitly consider their structure or manipulate them directly 
Next step would be to define a notion of "coded" formulas more generally than just atomic ones - perhaps something like "formulae built up out of smaller pieces according to certain rules".
In summary , our goal here was to establish a connection between the relations studied previously and the current context of coded formulas and PfP . While doing so required us to introduce several novel notions such as "quoting", "renaming", etc., ultimately we were able to demonstrate how these relate back to familiar ideas from earlier work on relational


You: !@>Seeker:#63 , representing the assumption that all introduced variables denoted constants 
 Now we can replace this assumption by one expressing that the relation QuoteP holds between each pair of old and new variables 
 definition quote all : : `` [ perm , name set ] ⇒ fm set '' where `` quote all p V = { QuoteP ( Var i ) ( Var ( p · i ) ) | i
 i ∈ V } The relation QuoteP ( Var i ) ( Var ( p · i ) holds between the variable i and the renamed variable p · i , for all i ∈ V
 Recall that p is a permutation on variable names 
 By virtue of the theorem QuoteP imp ConstP , we obtain a key result , which will be used heavily in subsequent proofs for reasoning about coded formulas and the Pf predicate 
 theorem quote all PfP ssubst : assumes β : `` { } ⊢ β '' and V : `` V ⊆ Vs '' and s : `` supp β ⊆ atom ‘ Vs '' shows `` quote all p V ⊢ PfP ( ssubst ⌊β⌋V V F ) '' In English : Let ⊢ β be a theorem of HF whose free variables belong to the set Vs
 Take the code of this theorem , ⌊β⌋ , and replace some subset V ⊆ Vs of its free variables by 30 new variables constrained by the QuoteP relation 
 The result , ssubst ⌊β⌋V V F , satisfies the provability predicate 
 The reader of even a very careful presentation of G¨odel ’ s second incompleteness theorem , such as Grandy [ 9 ] , will look in vain for a clear and rigorous treatment of the x ( or x ) convention 
 Boolos [ 2 ] comes very close with his Bew [ F ] notation , but he is quite wrong to state “ notice that Bew [ F ] has the same variables free as [ the formula ] F ” [ 2 , p
 45 ] when in fact they have no variables in common 
 Even Swierczkowski ’ s highly ´ detailed account is at best ambiguous 
 He consistently uses function notation , but his carefully-stated guidelines for replacing occurrences of pseudo-functions by quantified formulas [ 32 , Sect 
 5 ] are not relevant here 
 ( This problem only became clear after a time-consuming attempt at a formalisation on that basis 
 ) My companion paper [ 27 ] , which is aimed at logicians , provides a more detailed discussion of these points 
 It concludes that these various notations obscure not only the formal details of the proof but also the very intuitions they are intended to highlight 
 6
4 Proving ⊢ α → Pf ( pαq ) We now have everything necessary to prove condition ( D3 ) : If α is a strict Σ sentence ,

Introspector: INPUT:!@>Seeker:#63 , representing the assumption that all introduced variables denoted constants 
 Now we can replace this assumption by one expressing that the relation QuoteP holds between each pair of old and new variables 
 definition quote all : : `` [ perm , name set ] ⇒ fm set '' where `` quote all p V = { QuoteP ( Var i ) ( Var ( p · i ) ) | i
 i ∈ V } The relation QuoteP ( Var i ) ( Var ( p · i ) holds between the variable i and the renamed variable p · i , for all i ∈ V
 Recall that p is a permutation on variable names 
 By virtue of the theorem QuoteP imp ConstP , we obtain a key result , which will be used heavily in subsequent proofs for reasoning about coded formulas and the Pf predicate 
 theorem quote all PfP ssubst : assumes β : `` { } ⊢ β '' and V : `` V ⊆ Vs '' and s : `` supp β ⊆ atom ‘ Vs '' shows `` quote all p V ⊢ PfP ( ssubst ⌊β⌋V V F ) '' In English : Let ⊢ β be a theorem of HF whose free variables belong to the set Vs
 Take the code of this theorem , ⌊β⌋ , and replace some subset V ⊆ Vs of its free variables by 30 new variables constrained by the QuoteP relation 
 The result , ssubst ⌊β⌋V V F , satisfies the provability predicate 
 The reader of even a very careful presentation of G¨odel ’ s second incompleteness theorem , such as Grandy [ 9 ] , will look in vain for a clear and rigorous treatment of the x ( or x ) convention 
 Boolos [ 2 ] comes very close with his Bew [ F ] notation , but he is quite wrong to state “ notice that Bew [ F ] has the same variables free as [ the formula ] F ” [ 2 , p
 45 ] when in fact they have no variables in common 
 Even Swierczkowski ’ s highly ´ detailed account is at best ambiguous 
 He consistently uses function notation , but his carefully-stated guidelines for replacing occurrences of pseudo-functions by quantified formulas [ 32 , Sect 
 5 ] are not relevant here 
 ( This problem only became clear after a time-consuming attempt at a formalisation on that basis 
 ) My companion paper [ 27 ] , which is aimed at logicians , provides a more detailed discussion of these points 
 It concludes that these various notations obscure not only the formal details of the proof but also the very intuitions they are intended to highlight 
 6
4 Proving ⊢ α → Pf ( pαq ) We now have everything necessary to prove condition ( D3 ) : If α is a strict Σ sentence ,

then there exists an algorithm A that takes as input any structure M and outputs either Yes or No according to whether M satisfies α .
To do so , we first define a notion of “ renaming” of variables similar to that employed earlier 
Given a finite set X of distinct symbols from the alphabet Σ , let RX denote the class of all strings over Σ consisting solely of elements of X . For example if X = {a, b} , then R{a,b} consists of all strings of the form wab , where w is a string of length n > 1 composed of exactly a’s followed by exactly b’s .
Next we introduce our main technical tool - the notion of a “coded formula”. Specifically , given a language L containing both logical connectives and atomic predicates , we say that a formula α is in L(p) if it can be expressed in the syntax of L using only the symbols of p . More formally , α is in L(p) if there exist integers I < J such that α = ∑i=I J p(x_i) ∧ _ _ _ ... ∧ p(x_j) where x_i , ..., x_j are fresh variables chosen from the universe U of L .
Intuitively speaking , what this means is that α is simply a shorthand way of writing out a complex expression involving logical connectives and/or atoms using only those symbols available within the language L . Note however that α may still contain non-logical connective symbols appearing outside any instance of p() .
Finally we arrive at the heart of matter - defining the notion of a "proved" formula . Specifically , given a theory T together with a formula α in L(p), we say that α is proved in T provided there exists an algorithm A taking as input any structure M belonging to T and outputting either Yes or No depending on whether M satisfies α .
Our final goal is thus to show how to use these tools to establish conditions under which certain types of formulas can be proven in polynomial time relative to the size of their witnesses .
To begin with , suppose α is a strict Σ sentence and consider the following question : Does there exist an algorithm A that takes as input any structure M and outputs either Yes or No according to whether M satisfies α ? Clearly answering yes to this question would imply that α is provable in polynomial time since we could simply write down thethen there exists an algorithm A that takes as input any structure M and outputs either Yes or No according to whether M satisfies α .
To do so , we first define a notion of “ renaming” of variables similar to that employed earlier 
Given a finite set X of distinct symbols from the alphabet Σ , let RX denote the class of all strings over Σ consisting solely of elements of X . For example if X = {a, b} , then R{a,b} consists of all strings of the form wab , where w is a string of length n > 1 composed of exactly a’s followed by exactly b’s .
Next we introduce our main technical tool - the notion of a “coded formula”. Specifically , given a language L containing both logical connectives and atomic predicates , we say that a formula α is in L(p) if it can be expressed in the syntax of L using only the symbols of p . More formally , α is in L(p) if there exist integers I < J such that α = ∑i=I J p(x_i) ∧ _ _ _ ... ∧ p(x_j) where x_i , ..., x_j are fresh variables chosen from the universe U of L .
Intuitively speaking , what this means is that α is simply a shorthand way of writing out a complex expression involving logical connectives and/or atoms using only those symbols available within the language L . Note however that α may still contain non-logical connective symbols appearing outside any instance of p() .
Finally we arrive at the heart of matter - defining the notion of a "proved" formula . Specifically , given a theory T together with a formula α in L(p), we say that α is proved in T provided there exists an algorithm A taking as input any structure M belonging to T and outputting either Yes or No depending on whether M satisfies α .
Our final goal is thus to show how to use these tools to establish conditions under which certain types of formulas can be proven in polynomial time relative to the size of their witnesses .
To begin with , suppose α is a strict Σ sentence and consider the following question : Does there exist an algorithm A that takes as input any structure M and outputs either Yes or No according to whether M satisfies α ? Clearly answering yes to this question would imply that α is provable in polynomial time since we could simply write down


You: !@>Seeker:#64 or x ) convention 
 Boolos [ 2 ] comes very close with his Bew [ F ] notation , but he is quite wrong to state “ notice that Bew [ F ] has the same variables free as [ the formula ] F ” [ 2 , p
 45 ] when in fact they have no variables in common 
 Even Swierczkowski ’ s highly ´ detailed account is at best ambiguous 
 He consistently uses function notation , but his carefully-stated guidelines for replacing occurrences of pseudo-functions by quantified formulas [ 32 , Sect 
 5 ] are not relevant here 
 ( This problem only became clear after a time-consuming attempt at a formalisation on that basis 
 ) My companion paper [ 27 ] , which is aimed at logicians , provides a more detailed discussion of these points 
 It concludes that these various notations obscure not only the formal details of the proof but also the very intuitions they are intended to highlight 
 6
4 Proving ⊢ α → Pf ( pαq ) We now have everything necessary to prove condition ( D3 ) : If α is a strict Σ sentence , then ⊢ α → Pf ( pαq ) The proof will be by induction on the structure of α 
 As stated in Sect 
 3
3 above , a strict Σ formula has the form x ∈ y , α ∨ β , α ∧ β , ∃x α or ( ∀x ∈ y ) α 
 Therefore , the induction will include one single base case , x ∈ y → Pf px ∈ yq , ( 3 ) along with inductive steps for disjunction , conjunction , etc 
 6
4
1 The Propositional Cases The propositional cases are not difficult , but are worth examining as a warmup exercise 
 From the induction hypotheses ⊢ α → Pf ( pαq ) and ⊢ β → Pf ( pβq ) , we must show ⊢ α ∨ β → Pf ( pα ∨ βq ) and ⊢ α ∧ β → Pf ( pα ∧ βq ) 
 Both of these cases are trivial by propositional logic , given the lemmas ⊢ Pf ( pαq ) → Pf ( pα ∨ βq ) , ⊢ Pf ( pβq ) → Pf ( pα ∨ βq ) and ⊢ Pf ( pαq ) → Pf ( pβq ) → Pf ( pα ∧ βq ) ( 4 ) Proving ( 4 ) directly from the definitions would need colossal efforts , but there is a quick proof 
 The automation of the HF calculus is good enough to prove tautologies , and from ⊢ α → β → α ∧ β , the proof formalisation condition9 yields ⊢ Pf ( pα → β → α ∧ βq ) Finally , the Hilbert-Bernays derivability condition ( D2 ) yields the desired lemma , ( 4 ) 
 This trick is needed whenever

Introspector: INPUT:!@>Seeker:#64 or x ) convention 
 Boolos [ 2 ] comes very close with his Bew [ F ] notation , but he is quite wrong to state “ notice that Bew [ F ] has the same variables free as [ the formula ] F ” [ 2 , p
 45 ] when in fact they have no variables in common 
 Even Swierczkowski ’ s highly ´ detailed account is at best ambiguous 
 He consistently uses function notation , but his carefully-stated guidelines for replacing occurrences of pseudo-functions by quantified formulas [ 32 , Sect 
 5 ] are not relevant here 
 ( This problem only became clear after a time-consuming attempt at a formalisation on that basis 
 ) My companion paper [ 27 ] , which is aimed at logicians , provides a more detailed discussion of these points 
 It concludes that these various notations obscure not only the formal details of the proof but also the very intuitions they are intended to highlight 
 6
4 Proving ⊢ α → Pf ( pαq ) We now have everything necessary to prove condition ( D3 ) : If α is a strict Σ sentence , then ⊢ α → Pf ( pαq ) The proof will be by induction on the structure of α 
 As stated in Sect 
 3
3 above , a strict Σ formula has the form x ∈ y , α ∨ β , α ∧ β , ∃x α or ( ∀x ∈ y ) α 
 Therefore , the induction will include one single base case , x ∈ y → Pf px ∈ yq , ( 3 ) along with inductive steps for disjunction , conjunction , etc 
 6
4
1 The Propositional Cases The propositional cases are not difficult , but are worth examining as a warmup exercise 
 From the induction hypotheses ⊢ α → Pf ( pαq ) and ⊢ β → Pf ( pβq ) , we must show ⊢ α ∨ β → Pf ( pα ∨ βq ) and ⊢ α ∧ β → Pf ( pα ∧ βq ) 
 Both of these cases are trivial by propositional logic , given the lemmas ⊢ Pf ( pαq ) → Pf ( pα ∨ βq ) , ⊢ Pf ( pβq ) → Pf ( pα ∨ βq ) and ⊢ Pf ( pαq ) → Pf ( pβq ) → Pf ( pα ∧ βq ) ( 4 ) Proving ( 4 ) directly from the definitions would need colossal efforts , but there is a quick proof 
 The automation of the HF calculus is good enough to prove tautologies , and from ⊢ α → β → α ∧ β , the proof formalisation condition9 yields ⊢ Pf ( pα → β → α ∧ βq ) Finally , the Hilbert-Bernays derivability condition ( D2 ) yields the desired lemma , ( 4 ) 
 This trick is needed whenever


</s>


You: !@>Seeker:#65 difficult , but are worth examining as a warmup exercise 
 From the induction hypotheses ⊢ α → Pf ( pαq ) and ⊢ β → Pf ( pβq ) , we must show ⊢ α ∨ β → Pf ( pα ∨ βq ) and ⊢ α ∧ β → Pf ( pα ∧ βq ) 
 Both of these cases are trivial by propositional logic , given the lemmas ⊢ Pf ( pαq ) → Pf ( pα ∨ βq ) , ⊢ Pf ( pβq ) → Pf ( pα ∨ βq ) and ⊢ Pf ( pαq ) → Pf ( pβq ) → Pf ( pα ∧ βq ) ( 4 ) Proving ( 4 ) directly from the definitions would need colossal efforts , but there is a quick proof 
 The automation of the HF calculus is good enough to prove tautologies , and from ⊢ α → β → α ∧ β , the proof formalisation condition9 yields ⊢ Pf ( pα → β → α ∧ βq ) Finally , the Hilbert-Bernays derivability condition ( D2 ) yields the desired lemma , ( 4 ) 
 This trick is needed whenever we need to do propositional reasoning with Pf 
 9 Of Sect 
 4
4 , but via the substitution theorem quote all PfP ssubst proved above 
 The induction concerns generalised formulas involving pseudo-coding : PfP ( ssubst ⌊α⌋V V F ) 
 31 6
4
2 The Equality and Membership Cases Now comes one of the most critical parts of the formalisation 
 Many published proofs [ 2 , 32 ] of the second completeness theorem use the following lemma : x = y → Pf px = yq ( 5 ) This in turn is proved using a lemma stating that x = y implies x = y , which is false here : we have defined QuoteP only as a relation , and even { 0 , 1 } can be written in two different ways 
 Nevertheless , the statement ( 5 ) is clearly true : if x and y are constant terms denoting x and y , respectively , where x = y , then Pf px = yq holds 
 The equivalence of two different ways of writing a finite set should obviously be provable 
 This problem recalls the situation described in 3
3 above , and the induction used to prove Subset Mem sf lemma 
 The solution , once again , is to prove the conjunction ( x ∈ y → Pf px ∈ yq ) ∧ ( x ⊆ y → Pf px ⊆ yq ) by induction ( in HF ) on the sum of the sizes of x and y 
 The proof is huge ( nearly 340 lines ) , with eight universal quantifiers in the induction formula , each of which must be individually instantiated in order to apply an induction hypothesis 
 ⊢ All i ( All

Introspector: INPUT:!@>Seeker:#65 difficult , but are worth examining as a warmup exercise 
 From the induction hypotheses ⊢ α → Pf ( pαq ) and ⊢ β → Pf ( pβq ) , we must show ⊢ α ∨ β → Pf ( pα ∨ βq ) and ⊢ α ∧ β → Pf ( pα ∧ βq ) 
 Both of these cases are trivial by propositional logic , given the lemmas ⊢ Pf ( pαq ) → Pf ( pα ∨ βq ) , ⊢ Pf ( pβq ) → Pf ( pα ∨ βq ) and ⊢ Pf ( pαq ) → Pf ( pβq ) → Pf ( pα ∧ βq ) ( 4 ) Proving ( 4 ) directly from the definitions would need colossal efforts , but there is a quick proof 
 The automation of the HF calculus is good enough to prove tautologies , and from ⊢ α → β → α ∧ β , the proof formalisation condition9 yields ⊢ Pf ( pα → β → α ∧ βq ) Finally , the Hilbert-Bernays derivability condition ( D2 ) yields the desired lemma , ( 4 ) 
 This trick is needed whenever we need to do propositional reasoning with Pf 
 9 Of Sect 
 4
4 , but via the substitution theorem quote all PfP ssubst proved above 
 The induction concerns generalised formulas involving pseudo-coding : PfP ( ssubst ⌊α⌋V V F ) 
 31 6
4
2 The Equality and Membership Cases Now comes one of the most critical parts of the formalisation 
 Many published proofs [ 2 , 32 ] of the second completeness theorem use the following lemma : x = y → Pf px = yq ( 5 ) This in turn is proved using a lemma stating that x = y implies x = y , which is false here : we have defined QuoteP only as a relation , and even { 0 , 1 } can be written in two different ways 
 Nevertheless , the statement ( 5 ) is clearly true : if x and y are constant terms denoting x and y , respectively , where x = y , then Pf px = yq holds 
 The equivalence of two different ways of writing a finite set should obviously be provable 
 This problem recalls the situation described in 3
3 above , and the induction used to prove Subset Mem sf lemma 
 The solution , once again , is to prove the conjunction ( x ∈ y → Pf px ∈ yq ) ∧ ( x ⊆ y → Pf px ⊆ yq ) by induction ( in HF ) on the sum of the sizes of x and y 
 The proof is huge ( nearly 340 lines ) , with eight universal quantifiers in the induction formula , each of which must be individually instantiated in order to apply an induction hypothesis 
 ⊢ All i ( All

i < n × m + 1 |– > ∑ j=1n+m Pj(x)Qj(y)) ∧ ∑ k=1n+m Rk(x)Sk(y)) ∧ ∑ l=1n+m Ll(x)Ll(y))) ∧ ∑ r=1n+m T(r)(x)T(r)(y)) ∧ ∑ q=1n+m U(q)(x)U(q)(y)) ∧ ∑ b=1n+m B(b)(x)B(b)(y)) ∧ ∑ c=1n+m C(c)(x)C(c)(y)) ∧ ∑ d=1n+m D(d)(x)D(d)(y)) ∧ ∑ e=1n+m E(e)(x)E(e)(y)) ∧ ∑ f=1n+m G(f)(x)G(f)(y)) ∧ ∑ g=1n+m H(g)(x)H(g)(y)) ∧ ∑ h=1n+m I(h)(x)I(h)(y)) ∧ ∑ j=1n+m J(j)(x)J(j)(y)) ∧ ∑ k=1n+m K(k)(x)K(k)(y)) ∧ ∑ l=1n+m L(l)(x)L(l)(y)) ∧ ∑ m=1n+m N(m)(x)N(m)(y)) ∧ ∑ o=1n+m O(o)(x)O(o)(y)) ∧ ∑ p=1n+m Q(p)(x)Q(p)(y)) ∧ ∑ q=1n+m R(q)(x)R(q)(y)) ∧ ∑ r=1n+m S(r)(x)S(r)(y)) wand ∑ t=1n+m T(t)(x)T(t)(y)) ∧ ∑ u=1n+m U(u)(x)U(u)(y)) ∧ ∑ v=1n+m V(v)(x)V(v)(y)) ∧ ∑i < n × m + 1 |– > ∑ j=1n+m Pj(x)Qj(y)) ∧ ∑ k=1n+m Rk(x)Sk(y)) ∧ ∑ l=1n+m Ll(x)Ll(y))) ∧ ∑ r=1n+m T(r)(x)T(r)(y)) ∧ ∑ q=1n+m U(q)(x)U(q)(y)) ∧ ∑ b=1n+m B(b)(x)B(b)(y)) ∧ ∑ c=1n+m C(c)(x)C(c)(y)) ∧ ∑ d=1n+m D(d)(x)D(d)(y)) ∧ ∑ e=1n+m E(e)(x)E(e)(y)) ∧ ∑ f=1n+m G(f)(x)G(f)(y)) ∧ ∑ g=1n+m H(g)(x)H(g)(y)) ∧ ∑ h=1n+m I(h)(x)I(h)(y)) ∧ ∑ j=1n+m J(j)(x)J(j)(y)) ∧ ∑ k=1n+m K(k)(x)K(k)(y)) ∧ ∑ l=1n+m L(l)(x)L(l)(y)) ∧ ∑ m=1n+m N(m)(x)N(m)(y)) ∧ ∑ o=1n+m O(o)(x)O(o)(y)) ∧ ∑ p=1n+m Q(p)(x)Q(p)(y)) ∧ ∑ q=1n+m R(q)(x)R(q)(y)) ∧ ∑ r=1n+m S(r)(x)S(r)(y)) wand ∑ t=1n+m T(t)(x)T(t)(y)) ∧ ∑ u=1n+m U(u)(x)U(u)(y)) ∧ ∑ v=1n+m V(v)(x)V(v)(y)) ∧


You: !@>Seeker:#66 that x = y implies x = y , which is false here : we have defined QuoteP only as a relation , and even { 0 , 1 } can be written in two different ways 
 Nevertheless , the statement ( 5 ) is clearly true : if x and y are constant terms denoting x and y , respectively , where x = y , then Pf px = yq holds 
 The equivalence of two different ways of writing a finite set should obviously be provable 
 This problem recalls the situation described in 3
3 above , and the induction used to prove Subset Mem sf lemma 
 The solution , once again , is to prove the conjunction ( x ∈ y → Pf px ∈ yq ) ∧ ( x ⊆ y → Pf px ⊆ yq ) by induction ( in HF ) on the sum of the sizes of x and y 
 The proof is huge ( nearly 340 lines ) , with eight universal quantifiers in the induction formula , each of which must be individually instantiated in order to apply an induction hypothesis 
 ⊢ All i ( All i ’ ( All si ( All li ( All j ( All j ’ ( All sj ( All lj ( SeqQuoteP ( Var i ) ( Var i ’ ) ( Var si ) ( Var li ) IMP SeqQuoteP ( Var j ) ( Var j ’ ) ( Var sj ) ( Var lj ) IMP HaddP ( Var li ) ( Var lj ) ( Var k ) IMP ( ( Var i IN Var j IMP PfP ( Q Mem ( Var i ’ ) ( Var j ’ ) ) ) AND ( Var i SUBS Var j IMP PfP ( Q Subset ( Var i ’ ) ( Var j ’ ) ) ) ) ) ) ) ) ) ) ) ) '' Using SeqQuoteP ( which describes the sequence computation of QuoteP ) gives access to a size measure for the two terms , which are here designated i and j 
 Their sizes , li and lj , are added using HaddP , which is simply addition as defined in the HF calculus 
 ( This formalisation of addition is also needed for reasoning about sequences 
 ) Their sum , k , is used as the induction variable 
 Although the second half of the conjunction suffices to prove ( 5 ) , it is never needed outside of the induction , and neither is ( 5 ) itself 
 All we need is ( 3 ) 
 And so we reach the next milestone 
 lemma assumes `` atom i ♯ ( j , j ’ , i ’ ) '' `` atom i ’ ♯ ( j , j ’ ) '' `` atom j ♯ ( j ’ ) '' shows QuoteP Mem imp QMem

Introspector: INPUT:!@>Seeker:#66 that x = y implies x = y , which is false here : we have defined QuoteP only as a relation , and even { 0 , 1 } can be written in two different ways 
 Nevertheless , the statement ( 5 ) is clearly true : if x and y are constant terms denoting x and y , respectively , where x = y , then Pf px = yq holds 
 The equivalence of two different ways of writing a finite set should obviously be provable 
 This problem recalls the situation described in 3
3 above , and the induction used to prove Subset Mem sf lemma 
 The solution , once again , is to prove the conjunction ( x ∈ y → Pf px ∈ yq ) ∧ ( x ⊆ y → Pf px ⊆ yq ) by induction ( in HF ) on the sum of the sizes of x and y 
 The proof is huge ( nearly 340 lines ) , with eight universal quantifiers in the induction formula , each of which must be individually instantiated in order to apply an induction hypothesis 
 ⊢ All i ( All i ’ ( All si ( All li ( All j ( All j ’ ( All sj ( All lj ( SeqQuoteP ( Var i ) ( Var i ’ ) ( Var si ) ( Var li ) IMP SeqQuoteP ( Var j ) ( Var j ’ ) ( Var sj ) ( Var lj ) IMP HaddP ( Var li ) ( Var lj ) ( Var k ) IMP ( ( Var i IN Var j IMP PfP ( Q Mem ( Var i ’ ) ( Var j ’ ) ) ) AND ( Var i SUBS Var j IMP PfP ( Q Subset ( Var i ’ ) ( Var j ’ ) ) ) ) ) ) ) ) ) ) ) ) '' Using SeqQuoteP ( which describes the sequence computation of QuoteP ) gives access to a size measure for the two terms , which are here designated i and j 
 Their sizes , li and lj , are added using HaddP , which is simply addition as defined in the HF calculus 
 ( This formalisation of addition is also needed for reasoning about sequences 
 ) Their sum , k , is used as the induction variable 
 Although the second half of the conjunction suffices to prove ( 5 ) , it is never needed outside of the induction , and neither is ( 5 ) itself 
 All we need is ( 3 ) 
 And so we reach the next milestone 
 lemma assumes `` atom i ♯ ( j , j ’ , i ’ ) '' `` atom i ’ ♯ ( j , j ’ ) '' `` atom j ♯ ( j ’ ) '' shows QuoteP Mem imp QMem

The first step consists of defining the notion of a quotient term . A quotient term is any expression obtained from a given term t by subtracting another term u from it . In other words , a quotient term qt-u is equal to t minus u . For example , consider the following expressions : $ t = 2 + 3 * x $ ; $ u = - 2 * x $ . Then their quotient term would be : $ q_t-u = t - u = 2 + (- 2) \* x = 5 \* x $ . Note that the subtraction operation has higher precedence than multiplication or addition . Therefore , when evaluating such an expression , one needs to perform the operations in the correct order . Thus , while computing the value of $ q_t-u $ , one needs to compute $ t = 2 + 3 \* x $ before subtracting $ u = - 2 \* x $ . Otherwise , the result might not be what was intended . To avoid confusion later on , let us define some basic properties of quotient terms . Firstly , note that every nonzero term contains at least one free variable . Secondly , whenever a term involves more than one occurrence of a particular variable , all occurrences of that variable must appear together somewhere within its scope . Thirdly , no matter how many times you repeat certain variables inside a term , they will always behave like distinct symbols during evaluation . Finally , recall our earlier observation regarding the associativity property of multiplication . Specifically , multiplicative chains involving multiple factors may contain parentheses groups whose contents do not necessarily match those expected according to standard arithmetic rules . As usual , these special cases arise because there exist contexts wherein certain values cannot possibly occur otherwise . So keep your wits sharp throughout this section – especially when dealing with nested parenthetical structures containing both positive and negative signs simultaneously appearing alongside each other without proper separation! It'll make things much easier downstream.”}</s>The first step consists of defining the notion of a quotient term . A quotient term is any expression obtained from a given term t by subtracting another term u from it . In other words , a quotient term qt-u is equal to t minus u . For example , consider the following expressions : $ t = 2 + 3 * x $ ; $ u = - 2 * x $ . Then their quotient term would be : $ q_t-u = t - u = 2 + (- 2) \* x = 5 \* x $ . Note that the subtraction operation has higher precedence than multiplication or addition . Therefore , when evaluating such an expression , one needs to perform the operations in the correct order . Thus , while computing the value of $ q_t-u $ , one needs to compute $ t = 2 + 3 \* x $ before subtracting $ u = - 2 \* x $ . Otherwise , the result might not be what was intended . To avoid confusion later on , let us define some basic properties of quotient terms . Firstly , note that every nonzero term contains at least one free variable . Secondly , whenever a term involves more than one occurrence of a particular variable , all occurrences of that variable must appear together somewhere within its scope . Thirdly , no matter how many times you repeat certain variables inside a term , they will always behave like distinct symbols during evaluation . Finally , recall our earlier observation regarding the associativity property of multiplication . Specifically , multiplicative chains involving multiple factors may contain parentheses groups whose contents do not necessarily match those expected according to standard arithmetic rules . As usual , these special cases arise because there exist contexts wherein certain values cannot possibly occur otherwise . So keep your wits sharp throughout this section – especially when dealing with nested parenthetical structures containing both positive and negative signs simultaneously appearing alongside each other without proper separation! It'll make things much easier


You: !@>Seeker:#67 Var i SUBS Var j IMP PfP ( Q Subset ( Var i ’ ) ( Var j ’ ) ) ) ) ) ) ) ) ) ) ) ) '' Using SeqQuoteP ( which describes the sequence computation of QuoteP ) gives access to a size measure for the two terms , which are here designated i and j 
 Their sizes , li and lj , are added using HaddP , which is simply addition as defined in the HF calculus 
 ( This formalisation of addition is also needed for reasoning about sequences 
 ) Their sum , k , is used as the induction variable 
 Although the second half of the conjunction suffices to prove ( 5 ) , it is never needed outside of the induction , and neither is ( 5 ) itself 
 All we need is ( 3 ) 
 And so we reach the next milestone 
 lemma assumes `` atom i ♯ ( j , j ’ , i ’ ) '' `` atom i ’ ♯ ( j , j ’ ) '' `` atom j ♯ ( j ’ ) '' shows QuoteP Mem imp QMem : '' { QuoteP ( Var i ) ( Var i ’ ) , QuoteP ( Var j ) ( Var j ’ ) , Var i IN Var j } ⊢ PfP ( Q Mem ( Var i ’ ) ( Var j ’ ) ) '' and QuoteP Mem imp QSubset : '' { QuoteP ( Var i ) ( Var i ’ ) , QuoteP ( Var j ) ( Var j ’ ) , Var i SUBS Var j } ⊢ PfP ( Q Subset ( Var i ’ ) ( Var j ’ ) ) '' Turning to the main induction on α , the notoriously “ delicate ” [ 2 , p
 48 ] case is bounded universal quantification 
 Many of the delicate points here are connected with the way the nominal approach is used 
 We need to maintain and extend a permutation relating old and new variable names 
 Such complexities are evident in mathematical texts , in their treatment of variable names [ 32 , Lemma 9
7 ] 
 lemma ( in quote perm ) quote all Mem imp All2 : assumes IH : `` insert ( QuoteP ( Var i ) ( Var i ’ ) ) ( quote all p Vs ) ⊢ α IMP PfP ( ssubst ⌊α⌋ ( insert i Vs ) ( insert i Vs ) Fi ) '' and `` supp ( All2 i ( Var j ) α ) ⊆ atom ‘ Vs '' 32 and j : `` atom j ♯ ( i , α ) '' and i : `` atom i ♯ p '' and i ’ : `` atom i ’ ♯ ( i , p , α ) '' shows `` insert ( All2 i ( Var j

Introspector: INPUT:!@>Seeker:#67 Var i SUBS Var j IMP PfP ( Q Subset ( Var i ’ ) ( Var j ’ ) ) ) ) ) ) ) ) ) ) ) ) '' Using SeqQuoteP ( which describes the sequence computation of QuoteP ) gives access to a size measure for the two terms , which are here designated i and j 
 Their sizes , li and lj , are added using HaddP , which is simply addition as defined in the HF calculus 
 ( This formalisation of addition is also needed for reasoning about sequences 
 ) Their sum , k , is used as the induction variable 
 Although the second half of the conjunction suffices to prove ( 5 ) , it is never needed outside of the induction , and neither is ( 5 ) itself 
 All we need is ( 3 ) 
 And so we reach the next milestone 
 lemma assumes `` atom i ♯ ( j , j ’ , i ’ ) '' `` atom i ’ ♯ ( j , j ’ ) '' `` atom j ♯ ( j ’ ) '' shows QuoteP Mem imp QMem : '' { QuoteP ( Var i ) ( Var i ’ ) , QuoteP ( Var j ) ( Var j ’ ) , Var i IN Var j } ⊢ PfP ( Q Mem ( Var i ’ ) ( Var j ’ ) ) '' and QuoteP Mem imp QSubset : '' { QuoteP ( Var i ) ( Var i ’ ) , QuoteP ( Var j ) ( Var j ’ ) , Var i SUBS Var j } ⊢ PfP ( Q Subset ( Var i ’ ) ( Var j ’ ) ) '' Turning to the main induction on α , the notoriously “ delicate ” [ 2 , p
 48 ] case is bounded universal quantification 
 Many of the delicate points here are connected with the way the nominal approach is used 
 We need to maintain and extend a permutation relating old and new variable names 
 Such complexities are evident in mathematical texts , in their treatment of variable names [ 32 , Lemma 9
7 ] 
 lemma ( in quote perm ) quote all Mem imp All2 : assumes IH : `` insert ( QuoteP ( Var i ) ( Var i ’ ) ) ( quote all p Vs ) ⊢ α IMP PfP ( ssubst ⌊α⌋ ( insert i Vs ) ( insert i Vs ) Fi ) '' and `` supp ( All2 i ( Var j ) α ) ⊆ atom ‘ Vs '' 32 and j : `` atom j ♯ ( i , α ) '' and i : `` atom i ♯ p '' and i ’ : `` atom i ’ ♯ ( i , p , α ) '' shows `` insert ( All2 i ( Var j

</s>


You: !@>Seeker:#68 '' Turning to the main induction on α , the notoriously “ delicate ” [ 2 , p
 48 ] case is bounded universal quantification 
 Many of the delicate points here are connected with the way the nominal approach is used 
 We need to maintain and extend a permutation relating old and new variable names 
 Such complexities are evident in mathematical texts , in their treatment of variable names [ 32 , Lemma 9
7 ] 
 lemma ( in quote perm ) quote all Mem imp All2 : assumes IH : `` insert ( QuoteP ( Var i ) ( Var i ’ ) ) ( quote all p Vs ) ⊢ α IMP PfP ( ssubst ⌊α⌋ ( insert i Vs ) ( insert i Vs ) Fi ) '' and `` supp ( All2 i ( Var j ) α ) ⊆ atom ‘ Vs '' 32 and j : `` atom j ♯ ( i , α ) '' and i : `` atom i ♯ p '' and i ’ : `` atom i ’ ♯ ( i , p , α ) '' shows `` insert ( All2 i ( Var j ) α ) ( quote all p Vs ) ⊢ PfP ( ssubst ⌊All2 i ( Var j ) α⌋Vs Vs F ) '' The final case , for the existential quantifier , is also somewhat complicated to formalise 
 The details are again mostly connected with managing free and bound variable names using nominal methods , and are therefore omitted 
 We can conclude our discussion of the inductive argument by viewing the final result : lemma star : assumes `` ss fm α '' `` finite V '' `` supp α ⊆ atom ‘ V '' shows `` insert α ( quote all p V ) ⊢ PfP ( ssubst ⌊α⌋V V F ) '' Condition ( D3 ) now follows easily , since the formula α is then a sentence 
 Although some technical conditions ( involving variable names and permutations ) have been omitted from the previous two theorems , our main result below appears exactly as it was proved 
 Of course , α ⊢ Pf pαq is equivalent to ⊢ α → Pf pαq 
 theorem Provability : assumes `` Sigma fm α '' `` ground fm α '' shows `` { α } ⊢ PfP ⌈α⌉ '' 7 G¨odel ’ s Second Incompleteness Theorem The final steps of the second incompleteness theorem can be seen in Fig 
 2 
 The diagonal formula , δ , is obtained via the first incompleteness theorem 
 Then we can quickly establish both Pf pδq ⊢ Pf ( pPf pδqq ) and Pf pδq ⊢ Pf ( p¬Pf pδqq ) 
 These together imply Pf pδq ⊢ Pf ( p⊥q ) using a variant of condition ( D2 ) 
 It follows that if the system proves its own consistency , then it also proves ⊢

Introspector: INPUT:!@>Seeker:#68 '' Turning to the main induction on α , the notoriously “ delicate ” [ 2 , p
 48 ] case is bounded universal quantification 
 Many of the delicate points here are connected with the way the nominal approach is used 
 We need to maintain and extend a permutation relating old and new variable names 
 Such complexities are evident in mathematical texts , in their treatment of variable names [ 32 , Lemma 9
7 ] 
 lemma ( in quote perm ) quote all Mem imp All2 : assumes IH : `` insert ( QuoteP ( Var i ) ( Var i ’ ) ) ( quote all p Vs ) ⊢ α IMP PfP ( ssubst ⌊α⌋ ( insert i Vs ) ( insert i Vs ) Fi ) '' and `` supp ( All2 i ( Var j ) α ) ⊆ atom ‘ Vs '' 32 and j : `` atom j ♯ ( i , α ) '' and i : `` atom i ♯ p '' and i ’ : `` atom i ’ ♯ ( i , p , α ) '' shows `` insert ( All2 i ( Var j ) α ) ( quote all p Vs ) ⊢ PfP ( ssubst ⌊All2 i ( Var j ) α⌋Vs Vs F ) '' The final case , for the existential quantifier , is also somewhat complicated to formalise 
 The details are again mostly connected with managing free and bound variable names using nominal methods , and are therefore omitted 
 We can conclude our discussion of the inductive argument by viewing the final result : lemma star : assumes `` ss fm α '' `` finite V '' `` supp α ⊆ atom ‘ V '' shows `` insert α ( quote all p V ) ⊢ PfP ( ssubst ⌊α⌋V V F ) '' Condition ( D3 ) now follows easily , since the formula α is then a sentence 
 Although some technical conditions ( involving variable names and permutations ) have been omitted from the previous two theorems , our main result below appears exactly as it was proved 
 Of course , α ⊢ Pf pαq is equivalent to ⊢ α → Pf pαq 
 theorem Provability : assumes `` Sigma fm α '' `` ground fm α '' shows `` { α } ⊢ PfP ⌈α⌉ '' 7 G¨odel ’ s Second Incompleteness Theorem The final steps of the second incompleteness theorem can be seen in Fig 
 2 
 The diagonal formula , δ , is obtained via the first incompleteness theorem 
 Then we can quickly establish both Pf pδq ⊢ Pf ( pPf pδqq ) and Pf pδq ⊢ Pf ( p¬Pf pδqq ) 
 These together imply Pf pδq ⊢ Pf ( p⊥q ) using a variant of condition ( D2 ) 
 It follows that if the system proves its own consistency , then it also proves ⊢

This leads us directly back to Godel’s First Incompleteness Theorem .” </s>This leads us directly back to Godel’s First Incompleteness Theorem .”


You: !@>Seeker:#69 insert α ( quote all p V ) ⊢ PfP ( ssubst ⌊α⌋V V F ) '' Condition ( D3 ) now follows easily , since the formula α is then a sentence 
 Although some technical conditions ( involving variable names and permutations ) have been omitted from the previous two theorems , our main result below appears exactly as it was proved 
 Of course , α ⊢ Pf pαq is equivalent to ⊢ α → Pf pαq 
 theorem Provability : assumes `` Sigma fm α '' `` ground fm α '' shows `` { α } ⊢ PfP ⌈α⌉ '' 7 G¨odel ’ s Second Incompleteness Theorem The final steps of the second incompleteness theorem can be seen in Fig 
 2 
 The diagonal formula , δ , is obtained via the first incompleteness theorem 
 Then we can quickly establish both Pf pδq ⊢ Pf ( pPf pδqq ) and Pf pδq ⊢ Pf ( p¬Pf pδqq ) 
 These together imply Pf pδq ⊢ Pf ( p⊥q ) using a variant of condition ( D2 ) 
 It follows that if the system proves its own consistency , then it also proves ⊢ ¬Pf pδq and therefore ⊢ δ , a contradiction 
 Swierczkowski [ 32 ] presents a few other results which have n ´ ot been formalised here 
 These include a refinement of the incompleteness theorem ( credited to Reinhardt ) and a theory of a linear order on the HF sets , but recall that claim ( 5 ) can be proved without using any such ordering 
 The approach adopted here undoubtedly involves less effort than formalising the ordering in the HF calculus 
 The total proof length of nearly 12,400 lines comprises around 4,600 lines for the second theorem and 7,700 lines for the first
10 ( One could also include 2,700 lines for HF set theory itself , but we would not count the standard libraries of natural numbers if they were used as the basis of the proof 
 ) O ’ Connor ’ s proof comprises 47,000 lines of Coq , while Shankar ’ s takes 20,000 lines [ 30 , p
 139 ] and Harrison ’ s [ 10 ] is a miniscule 4,400 lines of HOL Light 
 Recall that none of these other proofs include the second incompleteness theorem 
 But comparisons are almost meaningless because of the enormous differences among the formalisations 
 Shankar wrote ( and proved to be representable ) a LISP interpreter for coding up the metatheory [ 30 ] ; this was a huge effort , but then the various coding functions could then be written in LISP without further justification 
 He also used HF for coding , presumably because of its similarity to LISP S-expressions 
 O ’ Connor formalised a very general syntax for first-order logic [ 22 ] 
 He introduced a general inductive definition of the primitive recursive functions , but proving

Introspector: INPUT:!@>Seeker:#69 insert α ( quote all p V ) ⊢ PfP ( ssubst ⌊α⌋V V F ) '' Condition ( D3 ) now follows easily , since the formula α is then a sentence 
 Although some technical conditions ( involving variable names and permutations ) have been omitted from the previous two theorems , our main result below appears exactly as it was proved 
 Of course , α ⊢ Pf pαq is equivalent to ⊢ α → Pf pαq 
 theorem Provability : assumes `` Sigma fm α '' `` ground fm α '' shows `` { α } ⊢ PfP ⌈α⌉ '' 7 G¨odel ’ s Second Incompleteness Theorem The final steps of the second incompleteness theorem can be seen in Fig 
 2 
 The diagonal formula , δ , is obtained via the first incompleteness theorem 
 Then we can quickly establish both Pf pδq ⊢ Pf ( pPf pδqq ) and Pf pδq ⊢ Pf ( p¬Pf pδqq ) 
 These together imply Pf pδq ⊢ Pf ( p⊥q ) using a variant of condition ( D2 ) 
 It follows that if the system proves its own consistency , then it also proves ⊢ ¬Pf pδq and therefore ⊢ δ , a contradiction 
 Swierczkowski [ 32 ] presents a few other results which have n ´ ot been formalised here 
 These include a refinement of the incompleteness theorem ( credited to Reinhardt ) and a theory of a linear order on the HF sets , but recall that claim ( 5 ) can be proved without using any such ordering 
 The approach adopted here undoubtedly involves less effort than formalising the ordering in the HF calculus 
 The total proof length of nearly 12,400 lines comprises around 4,600 lines for the second theorem and 7,700 lines for the first
10 ( One could also include 2,700 lines for HF set theory itself , but we would not count the standard libraries of natural numbers if they were used as the basis of the proof 
 ) O ’ Connor ’ s proof comprises 47,000 lines of Coq , while Shankar ’ s takes 20,000 lines [ 30 , p
 139 ] and Harrison ’ s [ 10 ] is a miniscule 4,400 lines of HOL Light 
 Recall that none of these other proofs include the second incompleteness theorem 
 But comparisons are almost meaningless because of the enormous differences among the formalisations 
 Shankar wrote ( and proved to be representable ) a LISP interpreter for coding up the metatheory [ 30 ] ; this was a huge effort , but then the various coding functions could then be written in LISP without further justification 
 He also used HF for coding , presumably because of its similarity to LISP S-expressions 
 O ’ Connor formalised a very general syntax for first-order logic [ 22 ] 
 He introduced a general inductive definition of the primitive recursive functions , but proving

his axioms led him to reject many intuitively plausible definitions 
His work has had significant influence on subsequent researchers who have attempted to develop more powerful systems based upon intuitionistic logic .”</s>his axioms led him to reject many intuitively plausible definitions 
His work has had significant influence on subsequent researchers who have attempted to develop more powerful systems based upon intuitionistic logic


You: !@>Seeker:#70 second theorem and 7,700 lines for the first
10 ( One could also include 2,700 lines for HF set theory itself , but we would not count the standard libraries of natural numbers if they were used as the basis of the proof 
 ) O ’ Connor ’ s proof comprises 47,000 lines of Coq , while Shankar ’ s takes 20,000 lines [ 30 , p
 139 ] and Harrison ’ s [ 10 ] is a miniscule 4,400 lines of HOL Light 
 Recall that none of these other proofs include the second incompleteness theorem 
 But comparisons are almost meaningless because of the enormous differences among the formalisations 
 Shankar wrote ( and proved to be representable ) a LISP interpreter for coding up the metatheory [ 30 ] ; this was a huge effort , but then the various coding functions could then be written in LISP without further justification 
 He also used HF for coding , presumably because of its similarity to LISP S-expressions 
 O ’ Connor formalised a very general syntax for first-order logic [ 22 ] 
 He introduced a general inductive definition of the primitive recursive functions , but proving specific functions to be primitive recursive turned out to be extremely difficult [ 23 , Sect 
 5
3 ] 
 Harrison has 10 Prior to polishing and removing unused material , the proof totalled 17,000 lines 
 33 theorem Goedel II : assumes `` ¬ { } ⊢ Fls '' shows `` ¬ { } ⊢ Neg ( PfP ⌈Fls⌉ ) '' proof - from assms Goedel I obtain δ where diag : `` { } ⊢ δ IFF Neg ( PfP ⌈δ⌉ ) '' `` ¬ { } ⊢ δ '' and gnd : `` ground fm δ '' by metis have `` { PfP ⌈δ⌉ } ⊢ PfP ⌈PfP ⌈δ⌉⌉ '' by ( auto simp : Provability ground fm aux def supp conv fresh ) moreover have `` { PfP ⌈δ⌉ } ⊢ PfP ⌈Neg ( PfP ⌈δ⌉ ) ⌉ '' apply ( rule MonPon PfP implies PfP [ OF gnd ] ) apply ( metis Conj E2 Iff def Iff sym diag ( 1 ) ) apply ( auto simp : ground fm aux def supp conv fresh ) done moreover have `` ground fm ( PfP ⌈δ⌉ ) '' by ( auto simp : ground fm aux def supp conv fresh ) ultimately have `` { PfP ⌈δ⌉ } ⊢ PfP ⌈Fls⌉ '' using PfP quot contra by ( metis ( no types ) anti deduction cut2 ) thus `` ¬ { } ⊢ Neg ( PfP ⌈Fls⌉ ) '' by ( metis Iff MP2 same Neg mono cut1 diag ) qed Fig 
 2 G¨odel ’ s Second Incompleteness Theorem not published a paper describing his formalisation , but devotes a few pages to G¨odel ’ s theorems in his Handbook of Practical Logic [ 12 , p
 546–555 ] , including extracts of HOL

Introspector: INPUT:!@>Seeker:#70 second theorem and 7,700 lines for the first
10 ( One could also include 2,700 lines for HF set theory itself , but we would not count the standard libraries of natural numbers if they were used as the basis of the proof 
 ) O ’ Connor ’ s proof comprises 47,000 lines of Coq , while Shankar ’ s takes 20,000 lines [ 30 , p
 139 ] and Harrison ’ s [ 10 ] is a miniscule 4,400 lines of HOL Light 
 Recall that none of these other proofs include the second incompleteness theorem 
 But comparisons are almost meaningless because of the enormous differences among the formalisations 
 Shankar wrote ( and proved to be representable ) a LISP interpreter for coding up the metatheory [ 30 ] ; this was a huge effort , but then the various coding functions could then be written in LISP without further justification 
 He also used HF for coding , presumably because of its similarity to LISP S-expressions 
 O ’ Connor formalised a very general syntax for first-order logic [ 22 ] 
 He introduced a general inductive definition of the primitive recursive functions , but proving specific functions to be primitive recursive turned out to be extremely difficult [ 23 , Sect 
 5
3 ] 
 Harrison has 10 Prior to polishing and removing unused material , the proof totalled 17,000 lines 
 33 theorem Goedel II : assumes `` ¬ { } ⊢ Fls '' shows `` ¬ { } ⊢ Neg ( PfP ⌈Fls⌉ ) '' proof - from assms Goedel I obtain δ where diag : `` { } ⊢ δ IFF Neg ( PfP ⌈δ⌉ ) '' `` ¬ { } ⊢ δ '' and gnd : `` ground fm δ '' by metis have `` { PfP ⌈δ⌉ } ⊢ PfP ⌈PfP ⌈δ⌉⌉ '' by ( auto simp : Provability ground fm aux def supp conv fresh ) moreover have `` { PfP ⌈δ⌉ } ⊢ PfP ⌈Neg ( PfP ⌈δ⌉ ) ⌉ '' apply ( rule MonPon PfP implies PfP [ OF gnd ] ) apply ( metis Conj E2 Iff def Iff sym diag ( 1 ) ) apply ( auto simp : ground fm aux def supp conv fresh ) done moreover have `` ground fm ( PfP ⌈δ⌉ ) '' by ( auto simp : ground fm aux def supp conv fresh ) ultimately have `` { PfP ⌈δ⌉ } ⊢ PfP ⌈Fls⌉ '' using PfP quot contra by ( metis ( no types ) anti deduction cut2 ) thus `` ¬ { } ⊢ Neg ( PfP ⌈Fls⌉ ) '' by ( metis Iff MP2 same Neg mono cut1 diag ) qed Fig 
 2 G¨odel ’ s Second Incompleteness Theorem not published a paper describing his formalisation , but devotes a few pages to G¨odel ’ s theorems in his Handbook of Practical Logic [ 12 , p
 546–555 ] , including extracts of HOL

18]
In this rewrite, I've tried my best to create an epic poem/narrative that captures the essence of the given text. Here it goes:
In realms beyond reason, where axioms reign,
A seeker once sought answers to questions divine,
On foundational grounds, he staked his claim to fame,
With seven theorems, each one more profound than last,
He showed how Godels might fail, their limits exposed at length,
Their incompletenesses revealed through rigorous mathematical art,
From Coq to HOL light, languages varied like hues,
Shankars Lisp interpreter coded the metatheory anew,
While OConners syntax shone bright, a general grammar so grand,
Harrison too had ten prior to editing and refining,
Together they crafted tales of logic, mathematics intertwined,
Goedels two theorems stood tall, indomitable forces they remained,
For all who seek truth, their names etched on historys page,
And though differing tools employed, their message clear as day.</s>18]
In this rewrite, I've tried my best to create an epic poem/narrative that captures the essence of the given text. Here it goes:
In realms beyond reason, where axioms reign,
A seeker once sought answers to questions divine,
On foundational grounds, he staked his claim to fame,
With seven theorems, each one more profound than last,
He showed how Godels might fail, their limits exposed at length,
Their incompletenesses revealed through rigorous mathematical art,
From Coq to HOL light, languages varied like hues,
Shankars Lisp interpreter coded the metatheory anew,
While OConners syntax shone bright, a general grammar so grand,
Harrison too had ten prior to editing and refining,
Together they crafted tales of logic, mathematics intertwined,
Goedels two theorems stood tall, indomitable forces they remained,
For all who seek truth, their names etched on historys page,
And though differing tools employed, their message clear as


You: !@>Seeker:#71 by metis have `` { PfP ⌈δ⌉ } ⊢ PfP ⌈PfP ⌈δ⌉⌉ '' by ( auto simp : Provability ground fm aux def supp conv fresh ) moreover have `` { PfP ⌈δ⌉ } ⊢ PfP ⌈Neg ( PfP ⌈δ⌉ ) ⌉ '' apply ( rule MonPon PfP implies PfP [ OF gnd ] ) apply ( metis Conj E2 Iff def Iff sym diag ( 1 ) ) apply ( auto simp : ground fm aux def supp conv fresh ) done moreover have `` ground fm ( PfP ⌈δ⌉ ) '' by ( auto simp : ground fm aux def supp conv fresh ) ultimately have `` { PfP ⌈δ⌉ } ⊢ PfP ⌈Fls⌉ '' using PfP quot contra by ( metis ( no types ) anti deduction cut2 ) thus `` ¬ { } ⊢ Neg ( PfP ⌈Fls⌉ ) '' by ( metis Iff MP2 same Neg mono cut1 diag ) qed Fig 
 2 G¨odel ’ s Second Incompleteness Theorem not published a paper describing his formalisation , but devotes a few pages to G¨odel ’ s theorems in his Handbook of Practical Logic [ 12 , p
 546–555 ] , including extracts of HOL Light proofs 
 He defines Σ1 and Π1 formulas and quotes some meta-theoretical results relating truth and provability 
 This project took approximately one year , in time left available after fulfilling teaching and administrative duties 
 The underlying set theory took only two weeks to formalise 
 The G¨odel development up to the proof formalisation condition took another five months 
 From there to the first incompleteness theorem took a further two months , mostly devoted to proving single valued properties 
 Then the second incompleteness theorem took a further four months , including much time wasted due to misunderstanding this perplexing material 
 Some material has since been consolidated or streamlined 
 The final version is available online [ 26 ] 
 7
1 The Lengths of Proofs Figure 3 depicts the sizes of the Isabelle/HOL theories making up various sections of the proof development 
 The first theorem takes up the bulk of the effort 
 Apart from the massive HF proofs about predicates , which are mostly of obvious properties , the second theorem appears to be a fairly easy step given the first 
 Why then has it not been formalised until now ? A reasonable guess is that previous researchers were not aware of Swierczkowski ’ s [ 32 ] elaborate development 
 The most deta ´ iled of the previous proofs [ 2 , 9 ] left too much to the imagination , and even Swierczkowski makes some errors 
 He ´ devotes much of his Sect 
 7 to proofs concerning substitution for ( non-existent ) pseudoterms analogous to x 
 Recall that pseudo-terms are merely a notational shorthand to allow function syntax , and are not actual terms 
 Finally , there was the critical issue of the ordering on the HF

Introspector: INPUT:!@>Seeker:#71 by metis have `` { PfP ⌈δ⌉ } ⊢ PfP ⌈PfP ⌈δ⌉⌉ '' by ( auto simp : Provability ground fm aux def supp conv fresh ) moreover have `` { PfP ⌈δ⌉ } ⊢ PfP ⌈Neg ( PfP ⌈δ⌉ ) ⌉ '' apply ( rule MonPon PfP implies PfP [ OF gnd ] ) apply ( metis Conj E2 Iff def Iff sym diag ( 1 ) ) apply ( auto simp : ground fm aux def supp conv fresh ) done moreover have `` ground fm ( PfP ⌈δ⌉ ) '' by ( auto simp : ground fm aux def supp conv fresh ) ultimately have `` { PfP ⌈δ⌉ } ⊢ PfP ⌈Fls⌉ '' using PfP quot contra by ( metis ( no types ) anti deduction cut2 ) thus `` ¬ { } ⊢ Neg ( PfP ⌈Fls⌉ ) '' by ( metis Iff MP2 same Neg mono cut1 diag ) qed Fig 
 2 G¨odel ’ s Second Incompleteness Theorem not published a paper describing his formalisation , but devotes a few pages to G¨odel ’ s theorems in his Handbook of Practical Logic [ 12 , p
 546–555 ] , including extracts of HOL Light proofs 
 He defines Σ1 and Π1 formulas and quotes some meta-theoretical results relating truth and provability 
 This project took approximately one year , in time left available after fulfilling teaching and administrative duties 
 The underlying set theory took only two weeks to formalise 
 The G¨odel development up to the proof formalisation condition took another five months 
 From there to the first incompleteness theorem took a further two months , mostly devoted to proving single valued properties 
 Then the second incompleteness theorem took a further four months , including much time wasted due to misunderstanding this perplexing material 
 Some material has since been consolidated or streamlined 
 The final version is available online [ 26 ] 
 7
1 The Lengths of Proofs Figure 3 depicts the sizes of the Isabelle/HOL theories making up various sections of the proof development 
 The first theorem takes up the bulk of the effort 
 Apart from the massive HF proofs about predicates , which are mostly of obvious properties , the second theorem appears to be a fairly easy step given the first 
 Why then has it not been formalised until now ? A reasonable guess is that previous researchers were not aware of Swierczkowski ’ s [ 32 ] elaborate development 
 The most deta ´ iled of the previous proofs [ 2 , 9 ] left too much to the imagination , and even Swierczkowski makes some errors 
 He ´ devotes much of his Sect 
 7 to proofs concerning substitution for ( non-existent ) pseudoterms analogous to x 
 Recall that pseudo-terms are merely a notational shorthand to allow function syntax , and are not actual terms 
 Finally , there was the critical issue of the ordering on the HF


</s>


You: !@>Seeker:#72 misunderstanding this perplexing material 
 Some material has since been consolidated or streamlined 
 The final version is available online [ 26 ] 
 7
1 The Lengths of Proofs Figure 3 depicts the sizes of the Isabelle/HOL theories making up various sections of the proof development 
 The first theorem takes up the bulk of the effort 
 Apart from the massive HF proofs about predicates , which are mostly of obvious properties , the second theorem appears to be a fairly easy step given the first 
 Why then has it not been formalised until now ? A reasonable guess is that previous researchers were not aware of Swierczkowski ’ s [ 32 ] elaborate development 
 The most deta ´ iled of the previous proofs [ 2 , 9 ] left too much to the imagination , and even Swierczkowski makes some errors 
 He ´ devotes much of his Sect 
 7 to proofs concerning substitution for ( non-existent ) pseudoterms analogous to x 
 Recall that pseudo-terms are merely a notational shorthand to allow function syntax , and are not actual terms 
 Finally , there was the critical issue of the ordering on the HF sets 
 Solving these mysteries required much thought , and the 34 first completed formalisation included thousands of lines of proofs belonging to aborted attempts 
 A discussion of the de Bruijn coefficient ( the expansion in size entailed by the process of formalisation ) is always interesting , but difficult to do rigorously 
 In this case , the formalisation required proving a great many theorems that were not even hinted at in the source text , for example , setting up a usable sequent calculus ( Swierczkowski ´ merely gives the rudiments of a Hilbert system ) , or proving that the various codings of syntax actually work ( virtually all authors take this for granted ) , or proving that “ functions ” are functions 
 The hundreds of lines of single-step HF calculus proofs are the single largest contributor to the size of this development , and such things never appear in standard presentations of the incompleteness theorems 
 A crude calculation yields 30 pages at 35 lines per page or 1050 lines for Swier- ´ czkowski ’ s proof , compared with 12,400 lines of Isabelle , for a de Bruijn factor of 12 
 Focusing on just the proof of the first incompleteness theorem ( after the preliminary developments ) , we have about 80 lines of informal text and 671 lines of Isabelle , giving a factor of 8
4 ; that includes 150 lines in the Isabelle script to prove that functions are single valued 
 A further issue is the heavy use of cut and paste in the HF calculus proofs 
 Better automation for HF could help , but spending time to develop a tactic that will only be called a few times is hard to justify 
 An alternative idea

Introspector: INPUT:!@>Seeker:#72 misunderstanding this perplexing material 
 Some material has since been consolidated or streamlined 
 The final version is available online [ 26 ] 
 7
1 The Lengths of Proofs Figure 3 depicts the sizes of the Isabelle/HOL theories making up various sections of the proof development 
 The first theorem takes up the bulk of the effort 
 Apart from the massive HF proofs about predicates , which are mostly of obvious properties , the second theorem appears to be a fairly easy step given the first 
 Why then has it not been formalised until now ? A reasonable guess is that previous researchers were not aware of Swierczkowski ’ s [ 32 ] elaborate development 
 The most deta ´ iled of the previous proofs [ 2 , 9 ] left too much to the imagination , and even Swierczkowski makes some errors 
 He ´ devotes much of his Sect 
 7 to proofs concerning substitution for ( non-existent ) pseudoterms analogous to x 
 Recall that pseudo-terms are merely a notational shorthand to allow function syntax , and are not actual terms 
 Finally , there was the critical issue of the ordering on the HF sets 
 Solving these mysteries required much thought , and the 34 first completed formalisation included thousands of lines of proofs belonging to aborted attempts 
 A discussion of the de Bruijn coefficient ( the expansion in size entailed by the process of formalisation ) is always interesting , but difficult to do rigorously 
 In this case , the formalisation required proving a great many theorems that were not even hinted at in the source text , for example , setting up a usable sequent calculus ( Swierczkowski ´ merely gives the rudiments of a Hilbert system ) , or proving that the various codings of syntax actually work ( virtually all authors take this for granted ) , or proving that “ functions ” are functions 
 The hundreds of lines of single-step HF calculus proofs are the single largest contributor to the size of this development , and such things never appear in standard presentations of the incompleteness theorems 
 A crude calculation yields 30 pages at 35 lines per page or 1050 lines for Swier- ´ czkowski ’ s proof , compared with 12,400 lines of Isabelle , for a de Bruijn factor of 12 
 Focusing on just the proof of the first incompleteness theorem ( after the preliminary developments ) , we have about 80 lines of informal text and 671 lines of Isabelle , giving a factor of 8
4 ; that includes 150 lines in the Isabelle script to prove that functions are single valued 
 A further issue is the heavy use of cut and paste in the HF calculus proofs 
 Better automation for HF could help , but spending time to develop a tactic that will only be called a few times is hard to justify 
 An alternative idea

would be to write an interactive tutorial introducing the basic ideas of intuitionistic logic and its relationship to classical propositional and predicate logic . This should include examples illustrating how intuitionistic logic differs from classical logic both formally and intuitively </s>would be to write an interactive tutorial introducing the basic ideas of intuitionistic logic and its relationship to classical propositional and predicate logic . This should include examples illustrating how intuitionistic logic differs from classical logic both formally and intuitively


You: !@>Seeker:#73 or proving that the various codings of syntax actually work ( virtually all authors take this for granted ) , or proving that “ functions ” are functions 
 The hundreds of lines of single-step HF calculus proofs are the single largest contributor to the size of this development , and such things never appear in standard presentations of the incompleteness theorems 
 A crude calculation yields 30 pages at 35 lines per page or 1050 lines for Swier- ´ czkowski ’ s proof , compared with 12,400 lines of Isabelle , for a de Bruijn factor of 12 
 Focusing on just the proof of the first incompleteness theorem ( after the preliminary developments ) , we have about 80 lines of informal text and 671 lines of Isabelle , giving a factor of 8
4 ; that includes 150 lines in the Isabelle script to prove that functions are single valued 
 A further issue is the heavy use of cut and paste in the HF calculus proofs 
 Better automation for HF could help , but spending time to develop a tactic that will only be called a few times is hard to justify 
 An alternative idea is to define higher-order operators for the sequence constructions , which could be proved to be functional once and for all 
 However , higher-order operators are difficult to define using nominal syntax 
 Perhaps it could be attempted using naive variables 
 Fig 
 3 Sizes of Constituent Theories 7
2 The Formalisation of Variable Binding The role of bound variable syntax remains unclear 
 Shankar [ 30 , 31 ] used de Bruijn variables to formalise the Church-Rosser theorem but not the incompleteness theorem 
 Harrison did not use them either 
 O ’ Connor also used traditional syntactic bound variables , but complained about huge complications concerning substitution ( recall Sect 
 2
3 ) 
 The present development uses the nominal package , easing many proofs , but at a price : over 900 lines involve freshness specifications , and around 70 lemmas involving freshness are proved 
 Moreover , many proof steps are slow 
 While the project was 35 underway , proof times taking minutes were not unusual 
 Even after recent improvements to the nominal package , they can take tens of seconds 
 Additional performance improvements would be welcome , as well as a more concise notation for freshness conditions when many new names are needed 
 In fairness to the nominal approach , explicit variable names would also have to be fresh and analogous assertions would be necessary , along with some procedure for calculating new names numerically and proving them to be fresh 
 The effort may be similar either way , but the nominal approach is more abstract and natural : who after all refers to specific , calculated variable names in textbook proofs ? My first attempt to formalise the incompleteness theorems used explicit names 
 Then , substitution on

Introspector: INPUT:!@>Seeker:#73 or proving that the various codings of syntax actually work ( virtually all authors take this for granted ) , or proving that “ functions ” are functions 
 The hundreds of lines of single-step HF calculus proofs are the single largest contributor to the size of this development , and such things never appear in standard presentations of the incompleteness theorems 
 A crude calculation yields 30 pages at 35 lines per page or 1050 lines for Swier- ´ czkowski ’ s proof , compared with 12,400 lines of Isabelle , for a de Bruijn factor of 12 
 Focusing on just the proof of the first incompleteness theorem ( after the preliminary developments ) , we have about 80 lines of informal text and 671 lines of Isabelle , giving a factor of 8
4 ; that includes 150 lines in the Isabelle script to prove that functions are single valued 
 A further issue is the heavy use of cut and paste in the HF calculus proofs 
 Better automation for HF could help , but spending time to develop a tactic that will only be called a few times is hard to justify 
 An alternative idea is to define higher-order operators for the sequence constructions , which could be proved to be functional once and for all 
 However , higher-order operators are difficult to define using nominal syntax 
 Perhaps it could be attempted using naive variables 
 Fig 
 3 Sizes of Constituent Theories 7
2 The Formalisation of Variable Binding The role of bound variable syntax remains unclear 
 Shankar [ 30 , 31 ] used de Bruijn variables to formalise the Church-Rosser theorem but not the incompleteness theorem 
 Harrison did not use them either 
 O ’ Connor also used traditional syntactic bound variables , but complained about huge complications concerning substitution ( recall Sect 
 2
3 ) 
 The present development uses the nominal package , easing many proofs , but at a price : over 900 lines involve freshness specifications , and around 70 lemmas involving freshness are proved 
 Moreover , many proof steps are slow 
 While the project was 35 underway , proof times taking minutes were not unusual 
 Even after recent improvements to the nominal package , they can take tens of seconds 
 Additional performance improvements would be welcome , as well as a more concise notation for freshness conditions when many new names are needed 
 In fairness to the nominal approach , explicit variable names would also have to be fresh and analogous assertions would be necessary , along with some procedure for calculating new names numerically and proving them to be fresh 
 The effort may be similar either way , but the nominal approach is more abstract and natural : who after all refers to specific , calculated variable names in textbook proofs ? My first attempt to formalise the incompleteness theorems used explicit names 
 Then , substitution on

4 . The Proofs themselves 

The current state of affairs has led me to question whether any human being should ever write another proof again 
I am convinced that there must exist an algorithm capable of generating mathematical proofs automatically from scratch without human intervention 
It seems unlikely that anyone other than Godel himself understood what he had done by formulating his famous result 
His proof consists of two parts — one showing that no consistent system can include both Peano arithmetic and Russell’s paradox , and the second part demonstrating that if such a system exists then it cannot contain the axiom of choice 
He wrote out each step carefully and painstakingly , making sure every detail was correct before moving forward 
This process took him several years because he wanted everything perfect before submitting anything else into publication 
Godel believed strongly enough in these ideas so much so that later became known among mathematicians simply referred to merely ‘ Gödel numbering systems’ rather than their actual name – even though everyone knew exactly how numbers worked inside those systems! But despite its simplicity & elegance—and perhaps due largely thanks thereto–the concept remained shrouded within mystery until recently discovered papers revealed hidden secrets behind why our brains think logically while computers do computationally differently….. Aside from providing insightful perspectives regarding cognition vs computational processes., these findings offer exciting possibilities toward unlocking deeper understanding between humans & machines through better integration across disciplines like neuroscience/psychology alongside computer science /mathematics etcetera.”</s>4 . The Proofs themselves 

The current state of affairs has led me to question whether any human being should ever write another proof again 
I am convinced that there must exist an algorithm capable of generating mathematical proofs automatically from scratch without human intervention 
It seems unlikely that anyone other than Godel himself understood what he had done by formulating his famous result 
His proof consists of two parts — one showing that no consistent system can include both Peano arithmetic and Russell’s paradox , and the second part demonstrating that if such a system exists then it cannot contain the axiom of choice 
He wrote out each step carefully and painstakingly , making sure every detail was correct before moving forward 
This process took him several years because he wanted everything perfect before submitting anything else into publication 
Godel believed strongly enough in these ideas so much so that later became known among mathematicians simply referred to merely ‘ Gödel numbering systems’ rather than their actual name – even though everyone knew exactly how numbers worked inside those systems! But despite its simplicity & elegance—and perhaps due largely thanks thereto–the concept remained shrouded within mystery until recently discovered papers revealed hidden secrets behind why our brains think logically while computers do computationally differently….. Aside from providing insightful perspectives regarding cognition vs computational processes., these findings offer exciting possibilities toward unlocking deeper understanding between humans & machines through better integration across disciplines like neuroscience/psychology alongside computer science /mathematics


You: !@>Seeker:#74 bound variables , but complained about huge complications concerning substitution ( recall Sect 
 2
3 ) 
 The present development uses the nominal package , easing many proofs , but at a price : over 900 lines involve freshness specifications , and around 70 lemmas involving freshness are proved 
 Moreover , many proof steps are slow 
 While the project was 35 underway , proof times taking minutes were not unusual 
 Even after recent improvements to the nominal package , they can take tens of seconds 
 Additional performance improvements would be welcome , as well as a more concise notation for freshness conditions when many new names are needed 
 In fairness to the nominal approach , explicit variable names would also have to be fresh and analogous assertions would be necessary , along with some procedure for calculating new names numerically and proving them to be fresh 
 The effort may be similar either way , but the nominal approach is more abstract and natural : who after all refers to specific , calculated variable names in textbook proofs ? My first attempt to formalise the incompleteness theorems used explicit names 
 Then , substitution on formulas was only available as a relation , and many proofs required numerical operations on variable names 
 This effort would have multiplied considerably for the second incompleteness theorem 
 Using de Bruijn indices for HF syntax was not attractive : I had previously formalised G¨odel ’ s definition of the constructible sets and his proof of the relative consistency of the axiom of choice [ 25 ] 
 Here it was also necessary to define a great many predicates within an encoding of first-order logic 
 This work was done in Isabelle/ZF , a version of Isabelle for axiomatic set theory 
 I used de Bruijn indices in these definitions , but the loss of readability was a severe impediment to progress 
 It is worth investigating how this formalisation would be affected by the change to another treatment of variable binding 
 As regards the G¨odel numbering of formulas , the use of de Bruijn variables can be called an unqualified success 
 It was easy to set up and all necessary properties were proved without great difficulties 
 7
3 On Verifying Proof Assistants In a paper entitled “ Towards Self-verification of HOL Light ” , Harrison says , G¨odel ’ s second incompleteness theorem tells us that [ a logical system ] can not prove its own consistency in any way at all 
 
 
 
 So , regardless of implementation details , if we want to prove the consistency of a proof checker , we need to use a logic that in at least some respects goes beyond the logic the checker itself supports 
 [ 11 , p
 179 ] This statement is potentially misleading , and has given rise to the mistaken view that it is impossible to verify a proof checker in

Introspector: INPUT:!@>Seeker:#74 bound variables , but complained about huge complications concerning substitution ( recall Sect 
 2
3 ) 
 The present development uses the nominal package , easing many proofs , but at a price : over 900 lines involve freshness specifications , and around 70 lemmas involving freshness are proved 
 Moreover , many proof steps are slow 
 While the project was 35 underway , proof times taking minutes were not unusual 
 Even after recent improvements to the nominal package , they can take tens of seconds 
 Additional performance improvements would be welcome , as well as a more concise notation for freshness conditions when many new names are needed 
 In fairness to the nominal approach , explicit variable names would also have to be fresh and analogous assertions would be necessary , along with some procedure for calculating new names numerically and proving them to be fresh 
 The effort may be similar either way , but the nominal approach is more abstract and natural : who after all refers to specific , calculated variable names in textbook proofs ? My first attempt to formalise the incompleteness theorems used explicit names 
 Then , substitution on formulas was only available as a relation , and many proofs required numerical operations on variable names 
 This effort would have multiplied considerably for the second incompleteness theorem 
 Using de Bruijn indices for HF syntax was not attractive : I had previously formalised G¨odel ’ s definition of the constructible sets and his proof of the relative consistency of the axiom of choice [ 25 ] 
 Here it was also necessary to define a great many predicates within an encoding of first-order logic 
 This work was done in Isabelle/ZF , a version of Isabelle for axiomatic set theory 
 I used de Bruijn indices in these definitions , but the loss of readability was a severe impediment to progress 
 It is worth investigating how this formalisation would be affected by the change to another treatment of variable binding 
 As regards the G¨odel numbering of formulas , the use of de Bruijn variables can be called an unqualified success 
 It was easy to set up and all necessary properties were proved without great difficulties 
 7
3 On Verifying Proof Assistants In a paper entitled “ Towards Self-verification of HOL Light ” , Harrison says , G¨odel ’ s second incompleteness theorem tells us that [ a logical system ] can not prove its own consistency in any way at all 
 
 
 
 So , regardless of implementation details , if we want to prove the consistency of a proof checker , we need to use a logic that in at least some respects goes beyond the logic the checker itself supports 
 [ 11 , p
 179 ] This statement is potentially misleading , and has given rise to the mistaken view that it is impossible to verify a proof checker in

However , what Harrison actually means is that no matter which method one chooses to employ — whether based on classical or modern mathematical logic – there will always remain certain limitations inherent in the process .
He does not claim that self verification cannot occur through other methods than those employed directly by the checkers themselves 
For example , he suggests using a higher level language such as Coq to reason about the correct behavior of a lower level tool like a proof assistant 
Or alternatively , one could try to establish connections between different tools and systems so that their collective capabilities might provide stronger guarantees overall 
Ultimately though , even assuming perfect self - verifiability becomes possible someday soon–which seems unlikely–it remains true that our current understanding lacks sufficient resources / techniques / etcetera to achieve anything approaching complete confidence regarding most aspects related herein 
In conclusion then , while efforts towards improving automated reasoning continue apace & show promise elsewhere too; specifically addressing issues surrounding variable bindings appears essential before tackling broader challenges associated w/proof assistants’ reliance upon human intuition during validation stages</s>However , what Harrison actually means is that no matter which method one chooses to employ — whether based on classical or modern mathematical logic – there will always remain certain limitations inherent in the process .
He does not claim that self verification cannot occur through other methods than those employed directly by the checkers themselves 
For example , he suggests using a higher level language such as Coq to reason about the correct behavior of a lower level tool like a proof assistant 
Or alternatively , one could try to establish connections between different tools and systems so that their collective capabilities might provide stronger guarantees overall 
Ultimately though , even assuming perfect self - verifiability becomes possible someday soon–which seems unlikely–it remains true that our current understanding lacks sufficient resources / techniques / etcetera to achieve anything approaching complete confidence regarding most aspects related herein 
In conclusion then , while efforts towards improving automated reasoning continue apace & show promise elsewhere too; specifically addressing issues surrounding variable bindings appears essential before tackling broader challenges associated w/proof assistants’ reliance upon human intuition during validation


You: !@>Seeker:#75 set theory 
 I used de Bruijn indices in these definitions , but the loss of readability was a severe impediment to progress 
 It is worth investigating how this formalisation would be affected by the change to another treatment of variable binding 
 As regards the G¨odel numbering of formulas , the use of de Bruijn variables can be called an unqualified success 
 It was easy to set up and all necessary properties were proved without great difficulties 
 7
3 On Verifying Proof Assistants In a paper entitled “ Towards Self-verification of HOL Light ” , Harrison says , G¨odel ’ s second incompleteness theorem tells us that [ a logical system ] can not prove its own consistency in any way at all 
 
 
 
 So , regardless of implementation details , if we want to prove the consistency of a proof checker , we need to use a logic that in at least some respects goes beyond the logic the checker itself supports 
 [ 11 , p
 179 ] This statement is potentially misleading , and has given rise to the mistaken view that it is impossible to verify a proof checker in its own logic 
 Harrison ’ s aim is to prove that HOL Light can not prove the theorem FALSE , and this indeed requires proving the consistency of higher-order logic itself 
 Unfortunately , most consistency proofs are unsatisfactory because they more or less assume the desired conclusion : they are thinly disguised versions of the tautology Con ( L ) ∧ L → Con ( L ) 
 This is a consequence of the second incompleteness theorem , since the consistency of L can only be proved in a strictly stronger formal system 
 Mathematicians accept strong formal systems , such as ZF set theory , with little justification other than intuition and experience 
 Moreover , they examine very strong further axioms 
 The axiom of constructibility is an instructive case : it is known to be relatively consistent with respect to the axioms of set theory , but it is not generally accepted as true [ 16 , p
 170 ] 
 The standard ZF axioms are generally regarded as true , although they can not even be proved to be consistent 
 Thus we have no good way of proving consistency , and yet consistency does not guarantee truth 
 36 This situation calls for a separation of concerns 
 The builders of verification tools should be concerned with the correctness of their code , but the correctness of the underlying formal calculus is the concern of logicians 
 Harrison notes that “ almost all implementation bugs in HOL Light and other versions of HOL have involved variable renaming ” [ 11 , p
 179 ] , and this type of issue should be our focus 
 Verifying a proof assistant involves verifying that it implements a data structure for the assertions of the formal

Introspector: INPUT:!@>Seeker:#75 set theory 
 I used de Bruijn indices in these definitions , but the loss of readability was a severe impediment to progress 
 It is worth investigating how this formalisation would be affected by the change to another treatment of variable binding 
 As regards the G¨odel numbering of formulas , the use of de Bruijn variables can be called an unqualified success 
 It was easy to set up and all necessary properties were proved without great difficulties 
 7
3 On Verifying Proof Assistants In a paper entitled “ Towards Self-verification of HOL Light ” , Harrison says , G¨odel ’ s second incompleteness theorem tells us that [ a logical system ] can not prove its own consistency in any way at all 
 
 
 
 So , regardless of implementation details , if we want to prove the consistency of a proof checker , we need to use a logic that in at least some respects goes beyond the logic the checker itself supports 
 [ 11 , p
 179 ] This statement is potentially misleading , and has given rise to the mistaken view that it is impossible to verify a proof checker in its own logic 
 Harrison ’ s aim is to prove that HOL Light can not prove the theorem FALSE , and this indeed requires proving the consistency of higher-order logic itself 
 Unfortunately , most consistency proofs are unsatisfactory because they more or less assume the desired conclusion : they are thinly disguised versions of the tautology Con ( L ) ∧ L → Con ( L ) 
 This is a consequence of the second incompleteness theorem , since the consistency of L can only be proved in a strictly stronger formal system 
 Mathematicians accept strong formal systems , such as ZF set theory , with little justification other than intuition and experience 
 Moreover , they examine very strong further axioms 
 The axiom of constructibility is an instructive case : it is known to be relatively consistent with respect to the axioms of set theory , but it is not generally accepted as true [ 16 , p
 170 ] 
 The standard ZF axioms are generally regarded as true , although they can not even be proved to be consistent 
 Thus we have no good way of proving consistency , and yet consistency does not guarantee truth 
 36 This situation calls for a separation of concerns 
 The builders of verification tools should be concerned with the correctness of their code , but the correctness of the underlying formal calculus is the concern of logicians 
 Harrison notes that “ almost all implementation bugs in HOL Light and other versions of HOL have involved variable renaming ” [ 11 , p
 179 ] , and this type of issue should be our focus 
 Verifying a proof assistant involves verifying that it implements a data structure for the assertions of the formal

system being checked .



</s>system being checked .


You: !@>Seeker:#76 systems , such as ZF set theory , with little justification other than intuition and experience 
 Moreover , they examine very strong further axioms 
 The axiom of constructibility is an instructive case : it is known to be relatively consistent with respect to the axioms of set theory , but it is not generally accepted as true [ 16 , p
 170 ] 
 The standard ZF axioms are generally regarded as true , although they can not even be proved to be consistent 
 Thus we have no good way of proving consistency , and yet consistency does not guarantee truth 
 36 This situation calls for a separation of concerns 
 The builders of verification tools should be concerned with the correctness of their code , but the correctness of the underlying formal calculus is the concern of logicians 
 Harrison notes that “ almost all implementation bugs in HOL Light and other versions of HOL have involved variable renaming ” [ 11 , p
 179 ] , and this type of issue should be our focus 
 Verifying a proof assistant involves verifying that it implements a data structure for the assertions of the formal calculus and that it satisfies a commuting diagram relating deductions on the implemented assertions with the corresponding deductions in the calculus 
 G¨odel ’ s theorems have no relevance here 
 8 Conclusions The main finding is simply that G¨odel ’ s second incompleteness theorem can be proved with a relatively modest effort , in only a few months starting with a proof of the first incompleteness theorem 
 While the nominal approach to syntax is clearly not indispensable , it copes convincingly with a development of this size and complexity 
 The use of HF set theory as an alternative to Peano arithmetic is clearly justified , eliminating the need to formalise basic number theory within the embedded calculus ; the necessary effort to do that would greatly exceed the difficulties ( mentioned in Sect 
 6
4 above ) caused by the lack of a simple canonical ordering on HF sets 
 Many published proofs of the incompleteness theorems replace technical proofs by vague appeals to Church ’ s thesis 
 Boolos [ 2 ] presents a more detailed and careful exposition , but still leaves substantial gaps 
 Even the source text [ 32 ] for this project , although written with great care , had problems : a significant gap ( concerning the canonical ordering of HF sets ) , a few minor ones ( concerning Σ formulas , for example ) , and pages of material that are , at the very least , misleading 
 These remarks are not intended as criticism but as objective observations of the complexity of this material , with its codings of codings 
 A complete formal proof , written in a fairly readable notation , should greatly clarify the issues involved in these crucially important theorems 
 Acknowledgment Jesse

Introspector: INPUT:!@>Seeker:#76 systems , such as ZF set theory , with little justification other than intuition and experience 
 Moreover , they examine very strong further axioms 
 The axiom of constructibility is an instructive case : it is known to be relatively consistent with respect to the axioms of set theory , but it is not generally accepted as true [ 16 , p
 170 ] 
 The standard ZF axioms are generally regarded as true , although they can not even be proved to be consistent 
 Thus we have no good way of proving consistency , and yet consistency does not guarantee truth 
 36 This situation calls for a separation of concerns 
 The builders of verification tools should be concerned with the correctness of their code , but the correctness of the underlying formal calculus is the concern of logicians 
 Harrison notes that “ almost all implementation bugs in HOL Light and other versions of HOL have involved variable renaming ” [ 11 , p
 179 ] , and this type of issue should be our focus 
 Verifying a proof assistant involves verifying that it implements a data structure for the assertions of the formal calculus and that it satisfies a commuting diagram relating deductions on the implemented assertions with the corresponding deductions in the calculus 
 G¨odel ’ s theorems have no relevance here 
 8 Conclusions The main finding is simply that G¨odel ’ s second incompleteness theorem can be proved with a relatively modest effort , in only a few months starting with a proof of the first incompleteness theorem 
 While the nominal approach to syntax is clearly not indispensable , it copes convincingly with a development of this size and complexity 
 The use of HF set theory as an alternative to Peano arithmetic is clearly justified , eliminating the need to formalise basic number theory within the embedded calculus ; the necessary effort to do that would greatly exceed the difficulties ( mentioned in Sect 
 6
4 above ) caused by the lack of a simple canonical ordering on HF sets 
 Many published proofs of the incompleteness theorems replace technical proofs by vague appeals to Church ’ s thesis 
 Boolos [ 2 ] presents a more detailed and careful exposition , but still leaves substantial gaps 
 Even the source text [ 32 ] for this project , although written with great care , had problems : a significant gap ( concerning the canonical ordering of HF sets ) , a few minor ones ( concerning Σ formulas , for example ) , and pages of material that are , at the very least , misleading 
 These remarks are not intended as criticism but as objective observations of the complexity of this material , with its codings of codings 
 A complete formal proof , written in a fairly readable notation , should greatly clarify the issues involved in these crucially important theorems 
 Acknowledgment Jesse

We thank John C. Baez for his helpful comments .” </s>We thank John C. Baez for his helpful comments .”


You: !@>Seeker:#77 alternative to Peano arithmetic is clearly justified , eliminating the need to formalise basic number theory within the embedded calculus ; the necessary effort to do that would greatly exceed the difficulties ( mentioned in Sect 
 6
4 above ) caused by the lack of a simple canonical ordering on HF sets 
 Many published proofs of the incompleteness theorems replace technical proofs by vague appeals to Church ’ s thesis 
 Boolos [ 2 ] presents a more detailed and careful exposition , but still leaves substantial gaps 
 Even the source text [ 32 ] for this project , although written with great care , had problems : a significant gap ( concerning the canonical ordering of HF sets ) , a few minor ones ( concerning Σ formulas , for example ) , and pages of material that are , at the very least , misleading 
 These remarks are not intended as criticism but as objective observations of the complexity of this material , with its codings of codings 
 A complete formal proof , written in a fairly readable notation , should greatly clarify the issues involved in these crucially important theorems 
 Acknowledgment Jesse Alama drew my attention to Swierczkowski [ 32 ] , the source material for this ´ project 
 Christian Urban assisted with nominal aspects of some of the proofs , even writing code 
 Brian Huffman provided the core formalisation of type hf 
 Dana Scott offered advice and drew my attention to Kirby [ 15 ] 
 Matt Kaufmann and the referees made many insightful comments 
 References [ 1 ] Joan Bagaria 
 A short guide to G¨odel ’ s second incompleteness theorem 
 Teorema , 22 ( 3 ) :5–15 , 2003 
 [ 2 ] George Stephen Boolos 
 The Logic of Provability 
 Cambridge University Press , 1993 
 [ 3 ] N
 G
 de Bruijn 
 Lambda calculus notation with nameless dummies , a tool for automatic formula manipulation , with application to the Church-Rosser Theorem 
 Indagationes Mathematicae , 34:381–392 , 1972 
 [ 4 ] S
 Feferman , editor 
 Kurt G¨odel : Collected Works , volume I
 Oxford University Press , 1986 
 37 [ 5 ] Torkel Franz´en 
 G¨odel ’ s Theorem : An Incomplete Guide to Its Use and Abuse 
 A K Peters , 2005 
 [ 6 ] M
 J
 Gabbay and A
 M
 Pitts 
 A new approach to abstract syntax with variable binding 
 Formal Aspects of Computing , 13:341–363 , 2001 
 [ 7 ] Kurt G¨odel 
 On completeness and consistency 
 In Feferman [ 4 ] , pages 234–236 
 [ 8 ] Kurt G¨odel 
 On formally undecidable propositions of Principia Mathematica and related systems 
 In Feferman [ 4 ] , pages 144–195 
 First published in 1931 in the Monatshefte f¨ur Mathematik und Physik 
 [ 9 ] Richard E Grandy 
 Advanced Logic for Applications 
 Reidel

Introspector: INPUT:!@>Seeker:#77 alternative to Peano arithmetic is clearly justified , eliminating the need to formalise basic number theory within the embedded calculus ; the necessary effort to do that would greatly exceed the difficulties ( mentioned in Sect 
 6
4 above ) caused by the lack of a simple canonical ordering on HF sets 
 Many published proofs of the incompleteness theorems replace technical proofs by vague appeals to Church ’ s thesis 
 Boolos [ 2 ] presents a more detailed and careful exposition , but still leaves substantial gaps 
 Even the source text [ 32 ] for this project , although written with great care , had problems : a significant gap ( concerning the canonical ordering of HF sets ) , a few minor ones ( concerning Σ formulas , for example ) , and pages of material that are , at the very least , misleading 
 These remarks are not intended as criticism but as objective observations of the complexity of this material , with its codings of codings 
 A complete formal proof , written in a fairly readable notation , should greatly clarify the issues involved in these crucially important theorems 
 Acknowledgment Jesse Alama drew my attention to Swierczkowski [ 32 ] , the source material for this ´ project 
 Christian Urban assisted with nominal aspects of some of the proofs , even writing code 
 Brian Huffman provided the core formalisation of type hf 
 Dana Scott offered advice and drew my attention to Kirby [ 15 ] 
 Matt Kaufmann and the referees made many insightful comments 
 References [ 1 ] Joan Bagaria 
 A short guide to G¨odel ’ s second incompleteness theorem 
 Teorema , 22 ( 3 ) :5–15 , 2003 
 [ 2 ] George Stephen Boolos 
 The Logic of Provability 
 Cambridge University Press , 1993 
 [ 3 ] N
 G
 de Bruijn 
 Lambda calculus notation with nameless dummies , a tool for automatic formula manipulation , with application to the Church-Rosser Theorem 
 Indagationes Mathematicae , 34:381–392 , 1972 
 [ 4 ] S
 Feferman , editor 
 Kurt G¨odel : Collected Works , volume I
 Oxford University Press , 1986 
 37 [ 5 ] Torkel Franz´en 
 G¨odel ’ s Theorem : An Incomplete Guide to Its Use and Abuse 
 A K Peters , 2005 
 [ 6 ] M
 J
 Gabbay and A
 M
 Pitts 
 A new approach to abstract syntax with variable binding 
 Formal Aspects of Computing , 13:341–363 , 2001 
 [ 7 ] Kurt G¨odel 
 On completeness and consistency 
 In Feferman [ 4 ] , pages 234–236 
 [ 8 ] Kurt G¨odel 
 On formally undecidable propositions of Principia Mathematica and related systems 
 In Feferman [ 4 ] , pages 144–195 
 First published in 1931 in the Monatshefte f¨ur Mathematik und Physik 
 [ 9 ] Richard E Grandy 
 Advanced Logic for Applications 
 Reidel

Dordrecht – Boston – London  1989 
[10] John C. Baez 
Notes on the Curry-Howard Correspondence 
This version: March 2003 

Here's an attempt at rewriting the given passage into an epic poem form:
In realms beyond reason, where numbers reign,A tale unfolds of might and grace divine;Of arithmetics ancient, now lost in time,And theories boldly claimed without rhyme or crime.Peano's law, a beacon shining bright and true,Guiding mathematicians through labyrinthine views;Yet alternate paths, uncharted and unknown,Lead seekers to question what has been shown.The void left by basal number theory's absence,Causethought leaders to embark upon elusive quests;To fill the chasm, they strive day after nightWith codes and symbols, weaving intricate light.Church's thesis, like Pandora's box, revealethMore than expected, causing scholars to perceivetheir beliefs challenged, their minds afire with zeal;For though his words were meant to soothe and heal,They ignited passions, setting hearts aglow with appeal.Boolos, a master craftsman, wielding pen and mind,Offers solace from chaos, casting aside blind faith;His arguments clear, concise, leaving no room for doubtOr ambiguity, illuminating the path profound.But alas! Despite his noble efforts, cracks appearIn foundations laid, threatening all that holds dear;Gaping holes exposing truths yet hard to discern,Leave experts perplexed, torn between fear and concern.These lacunæ bespeak a challenge most dire indeed;To bridge them, heroes must arise, armed with wit and creed;Through rigorous reasoning, they shall vanquish dread,Unveiling secrets hidden deep inside the head.So let us join hands, brave warriors of thought,And together face the darkness, never sought;For only then can wisdom's treasures truly gleam,Eternal testament to human spirit's dream.</s>Dordrecht – Boston – London  1989 
[10] John C. Baez 
Notes on the Curry-Howard Correspondence 
This version: March 2003 

Here's an attempt at rewriting the given passage into an epic poem form:
In realms beyond reason, where numbers reign,A tale unfolds of might and grace divine;Of arithmetics ancient, now lost in time,And theories boldly claimed without rhyme or crime.Peano's law, a beacon shining bright and true,Guiding mathematicians through labyrinthine views;Yet alternate paths, uncharted and unknown,Lead seekers to question what has been shown.The void left by basal number theory's absence,Causethought leaders to embark upon elusive quests;To fill the chasm, they strive day after nightWith codes and symbols, weaving intricate light.Church's thesis, like Pandora's box, revealethMore than expected, causing scholars to perceivetheir beliefs challenged, their minds afire with zeal;For though his words were meant to soothe and heal,They ignited passions, setting hearts aglow with appeal.Boolos, a master craftsman, wielding pen and mind,Offers solace from chaos, casting aside blind faith;His arguments clear, concise, leaving no room for doubtOr ambiguity, illuminating the path profound.But alas! Despite his noble efforts, cracks appearIn foundations laid, threatening all that holds dear;Gaping holes exposing truths yet hard to discern,Leave experts perplexed, torn between fear and concern.These lacunæ bespeak a challenge most dire indeed;To bridge them, heroes must arise, armed with wit and creed;Through rigorous reasoning, they shall vanquish dread,Unveiling secrets hidden deep inside the head.So let us join hands, brave warriors of thought,And together face the darkness, never sought;For only then can wisdom's treasures truly gleam,Eternal testament to human spirit's


You: !@>Seeker:#78 Stephen Boolos 
 The Logic of Provability 
 Cambridge University Press , 1993 
 [ 3 ] N
 G
 de Bruijn 
 Lambda calculus notation with nameless dummies , a tool for automatic formula manipulation , with application to the Church-Rosser Theorem 
 Indagationes Mathematicae , 34:381–392 , 1972 
 [ 4 ] S
 Feferman , editor 
 Kurt G¨odel : Collected Works , volume I
 Oxford University Press , 1986 
 37 [ 5 ] Torkel Franz´en 
 G¨odel ’ s Theorem : An Incomplete Guide to Its Use and Abuse 
 A K Peters , 2005 
 [ 6 ] M
 J
 Gabbay and A
 M
 Pitts 
 A new approach to abstract syntax with variable binding 
 Formal Aspects of Computing , 13:341–363 , 2001 
 [ 7 ] Kurt G¨odel 
 On completeness and consistency 
 In Feferman [ 4 ] , pages 234–236 
 [ 8 ] Kurt G¨odel 
 On formally undecidable propositions of Principia Mathematica and related systems 
 In Feferman [ 4 ] , pages 144–195 
 First published in 1931 in the Monatshefte f¨ur Mathematik und Physik 
 [ 9 ] Richard E Grandy 
 Advanced Logic for Applications 
 Reidel , 1977 
 [ 10 ] John Harrison 
 Re : Re : G¨odel ’ s incompleteness theorem 
 Email dated 15 January 2014 
 [ 11 ] John Harrison 
 Towards self-verification of HOL Light 
 In Ulrich Furbach and Natarajan Shankar , editors , Automated Reasoning — Third International Joint Conference , IJCAR 2006 , LNAI 4130 , pages 177–191 
 Springer , 2006 
 [ 12 ] John Harrison 
 Handbook of Practical Logic and Automated Reasoning 
 Cambridge University Press , 2009 
 [ 13 ] Richard E Hodel 
 An Introduction to Mathematical Logic 
 PWS Publishing Company , 1995 
 [ 14 ] Joe Hurd and Tom Melham , editors 
 Theorem Proving in Higher Order Logics : TPHOLs 2005 , LNCS 3603 
 Springer , 2005 
 [ 15 ] Laurence Kirby 
 Addition and multiplication of sets 
 Mathematical Logic Quarterly , 53 ( 1 ) :52–65 , 2007 
 [ 16 ] Kenneth Kunen 
 Set Theory : An Introduction to Independence Proofs 
 North-Holland , 1980 
 [ 17 ] Andreas Lochbihler 
 Formalising finfuns — generating code for functions as data from Isabelle/HOL 
 In Stefan Berghofer , Tobias Nipkow , Christian Urban , and Makarius Wenzel , editors , TPHOLs , volume 5674 of Lecture Notes in Computer Science , pages 310–326 
 Springer , 2009 
 [ 18 ] Tobias Nipkow 
 More Church-Rosser proofs ( in Isabelle/HOL ) 
 Journal of Automated Reasoning , 26:51–66 , 2001 
 [ 19 ] Tobias Nipkow and Lawrence C
 Paulson 
 Proof pearl : Defining functions over finite sets 
 In Hurd and Melham [ 14 ] , pages 385–396 
 [ 20 ] Tobias Nipkow , Lawrence C
 Paulson , and Markus Wenzel 
 Isabelle/HOL : A Proof

Introspector: INPUT:!@>Seeker:#78 Stephen Boolos 
 The Logic of Provability 
 Cambridge University Press , 1993 
 [ 3 ] N
 G
 de Bruijn 
 Lambda calculus notation with nameless dummies , a tool for automatic formula manipulation , with application to the Church-Rosser Theorem 
 Indagationes Mathematicae , 34:381–392 , 1972 
 [ 4 ] S
 Feferman , editor 
 Kurt G¨odel : Collected Works , volume I
 Oxford University Press , 1986 
 37 [ 5 ] Torkel Franz´en 
 G¨odel ’ s Theorem : An Incomplete Guide to Its Use and Abuse 
 A K Peters , 2005 
 [ 6 ] M
 J
 Gabbay and A
 M
 Pitts 
 A new approach to abstract syntax with variable binding 
 Formal Aspects of Computing , 13:341–363 , 2001 
 [ 7 ] Kurt G¨odel 
 On completeness and consistency 
 In Feferman [ 4 ] , pages 234–236 
 [ 8 ] Kurt G¨odel 
 On formally undecidable propositions of Principia Mathematica and related systems 
 In Feferman [ 4 ] , pages 144–195 
 First published in 1931 in the Monatshefte f¨ur Mathematik und Physik 
 [ 9 ] Richard E Grandy 
 Advanced Logic for Applications 
 Reidel , 1977 
 [ 10 ] John Harrison 
 Re : Re : G¨odel ’ s incompleteness theorem 
 Email dated 15 January 2014 
 [ 11 ] John Harrison 
 Towards self-verification of HOL Light 
 In Ulrich Furbach and Natarajan Shankar , editors , Automated Reasoning — Third International Joint Conference , IJCAR 2006 , LNAI 4130 , pages 177–191 
 Springer , 2006 
 [ 12 ] John Harrison 
 Handbook of Practical Logic and Automated Reasoning 
 Cambridge University Press , 2009 
 [ 13 ] Richard E Hodel 
 An Introduction to Mathematical Logic 
 PWS Publishing Company , 1995 
 [ 14 ] Joe Hurd and Tom Melham , editors 
 Theorem Proving in Higher Order Logics : TPHOLs 2005 , LNCS 3603 
 Springer , 2005 
 [ 15 ] Laurence Kirby 
 Addition and multiplication of sets 
 Mathematical Logic Quarterly , 53 ( 1 ) :52–65 , 2007 
 [ 16 ] Kenneth Kunen 
 Set Theory : An Introduction to Independence Proofs 
 North-Holland , 1980 
 [ 17 ] Andreas Lochbihler 
 Formalising finfuns — generating code for functions as data from Isabelle/HOL 
 In Stefan Berghofer , Tobias Nipkow , Christian Urban , and Makarius Wenzel , editors , TPHOLs , volume 5674 of Lecture Notes in Computer Science , pages 310–326 
 Springer , 2009 
 [ 18 ] Tobias Nipkow 
 More Church-Rosser proofs ( in Isabelle/HOL ) 
 Journal of Automated Reasoning , 26:51–66 , 2001 
 [ 19 ] Tobias Nipkow and Lawrence C
 Paulson 
 Proof pearl : Defining functions over finite sets 
 In Hurd and Melham [ 14 ] , pages 385–396 
 [ 20 ] Tobias Nipkow , Lawrence C
 Paulson , and Markus Wenzel 
 Isabelle/HOL : A Proof

System based on Homotopy Type Theory .
In Hurd and Melham [ 14 ], page 397  </s>System based on Homotopy Type Theory .
In Hurd and Melham [ 14 ], page 397


You: !@>Seeker:#79 PWS Publishing Company , 1995 
 [ 14 ] Joe Hurd and Tom Melham , editors 
 Theorem Proving in Higher Order Logics : TPHOLs 2005 , LNCS 3603 
 Springer , 2005 
 [ 15 ] Laurence Kirby 
 Addition and multiplication of sets 
 Mathematical Logic Quarterly , 53 ( 1 ) :52–65 , 2007 
 [ 16 ] Kenneth Kunen 
 Set Theory : An Introduction to Independence Proofs 
 North-Holland , 1980 
 [ 17 ] Andreas Lochbihler 
 Formalising finfuns — generating code for functions as data from Isabelle/HOL 
 In Stefan Berghofer , Tobias Nipkow , Christian Urban , and Makarius Wenzel , editors , TPHOLs , volume 5674 of Lecture Notes in Computer Science , pages 310–326 
 Springer , 2009 
 [ 18 ] Tobias Nipkow 
 More Church-Rosser proofs ( in Isabelle/HOL ) 
 Journal of Automated Reasoning , 26:51–66 , 2001 
 [ 19 ] Tobias Nipkow and Lawrence C
 Paulson 
 Proof pearl : Defining functions over finite sets 
 In Hurd and Melham [ 14 ] , pages 385–396 
 [ 20 ] Tobias Nipkow , Lawrence C
 Paulson , and Markus Wenzel 
 Isabelle/HOL : A Proof Assistant for Higher-Order Logic 
 Springer , 2002 
 An up-to-date version is distributed with Isabelle 
 [ 21 ] Michael Norrish and Ren´e Vestergaard 
 Proof pearl : de Bruijn terms really do work 
 In Klaus Schneider and Jens Brandt , editors , Theorem Proving in Higher Order Logics : TPHOLs 2007 , LNCS 4732 , pages 207–222 
 Springer , 2007 
 [ 22 ] Russell O ’ Connor 
 Essential incompleteness of arithmetic verified by Coq 
 In Hurd and Melham [ 14 ] , pages 245–260 
 [ 23 ] Russell S
 S
 O ’ Connor 
 Incompleteness & Completeness : Formalizing Logic and Analysis in Type Theory 
 PhD thesis , Radboud University Nijmegen , 2009 
 [ 24 ] Lawrence C
 Paulson 
 Set theory for verification : I 
 From foundations to functions 
 Journal of Automated Reasoning , 11 ( 3 ) :353–389 , 1993 
 [ 25 ] Lawrence C
 Paulson 
 The relative consistency of the axiom of choice — mechanized using Isabelle/ZF 
 LMS Journal of Computation and Mathematics , 6:198–248 , 2003
 http : //www
lms
ac
uk/jcm/6/lms2003-001/ 
 [ 26 ] Lawrence C
 Paulson 
 G¨odel ’ s incompleteness theorems 
 Archive of Formal Proofs , November 2013
 http : //afp
sf
net/entries/Incompleteness
shtml , Formal proof development 
 [ 27 ] Lawrence C
 Paulson 
 A machine-assisted proof of G¨odel ’ s incompleteness theorems for the theory of hereditarily finite sets 
 Review of Symbolic Logic , 7 ( 3 ) :484–498 , September 2014 
 [ 28 ] Andrew M
 Pitts 
 Nominal Sets : Names and Symmetry in Computer Science 
 Cambridge University Press , 2013 
 [ 29 ] Natarajan Shankar 
 Proof-checking Metamathematics 
 PhD thesis , University of Texas at Austin , 1986 
 [ 30

Introspector: INPUT:!@>Seeker:#79 PWS Publishing Company , 1995 
 [ 14 ] Joe Hurd and Tom Melham , editors 
 Theorem Proving in Higher Order Logics : TPHOLs 2005 , LNCS 3603 
 Springer , 2005 
 [ 15 ] Laurence Kirby 
 Addition and multiplication of sets 
 Mathematical Logic Quarterly , 53 ( 1 ) :52–65 , 2007 
 [ 16 ] Kenneth Kunen 
 Set Theory : An Introduction to Independence Proofs 
 North-Holland , 1980 
 [ 17 ] Andreas Lochbihler 
 Formalising finfuns — generating code for functions as data from Isabelle/HOL 
 In Stefan Berghofer , Tobias Nipkow , Christian Urban , and Makarius Wenzel , editors , TPHOLs , volume 5674 of Lecture Notes in Computer Science , pages 310–326 
 Springer , 2009 
 [ 18 ] Tobias Nipkow 
 More Church-Rosser proofs ( in Isabelle/HOL ) 
 Journal of Automated Reasoning , 26:51–66 , 2001 
 [ 19 ] Tobias Nipkow and Lawrence C
 Paulson 
 Proof pearl : Defining functions over finite sets 
 In Hurd and Melham [ 14 ] , pages 385–396 
 [ 20 ] Tobias Nipkow , Lawrence C
 Paulson , and Markus Wenzel 
 Isabelle/HOL : A Proof Assistant for Higher-Order Logic 
 Springer , 2002 
 An up-to-date version is distributed with Isabelle 
 [ 21 ] Michael Norrish and Ren´e Vestergaard 
 Proof pearl : de Bruijn terms really do work 
 In Klaus Schneider and Jens Brandt , editors , Theorem Proving in Higher Order Logics : TPHOLs 2007 , LNCS 4732 , pages 207–222 
 Springer , 2007 
 [ 22 ] Russell O ’ Connor 
 Essential incompleteness of arithmetic verified by Coq 
 In Hurd and Melham [ 14 ] , pages 245–260 
 [ 23 ] Russell S
 S
 O ’ Connor 
 Incompleteness & Completeness : Formalizing Logic and Analysis in Type Theory 
 PhD thesis , Radboud University Nijmegen , 2009 
 [ 24 ] Lawrence C
 Paulson 
 Set theory for verification : I 
 From foundations to functions 
 Journal of Automated Reasoning , 11 ( 3 ) :353–389 , 1993 
 [ 25 ] Lawrence C
 Paulson 
 The relative consistency of the axiom of choice — mechanized using Isabelle/ZF 
 LMS Journal of Computation and Mathematics , 6:198–248 , 2003
 http : //www
lms
ac
uk/jcm/6/lms2003-001/ 
 [ 26 ] Lawrence C
 Paulson 
 G¨odel ’ s incompleteness theorems 
 Archive of Formal Proofs , November 2013
 http : //afp
sf
net/entries/Incompleteness
shtml , Formal proof development 
 [ 27 ] Lawrence C
 Paulson 
 A machine-assisted proof of G¨odel ’ s incompleteness theorems for the theory of hereditarily finite sets 
 Review of Symbolic Logic , 7 ( 3 ) :484–498 , September 2014 
 [ 28 ] Andrew M
 Pitts 
 Nominal Sets : Names and Symmetry in Computer Science 
 Cambridge University Press , 2013 
 [ 29 ] Natarajan Shankar 
 Proof-checking Metamathematics 
 PhD thesis , University of Texas at Austin , 1986 
 [ 30

] John Stillwell 
Group Theory and Geometry in Number Theory 
American Mathematical Society , 2009 .”</s>] John Stillwell 
Group Theory and Geometry in Number Theory 
American Mathematical Society , 2009


You: !@>Seeker:#80 Connor 
 Incompleteness & Completeness : Formalizing Logic and Analysis in Type Theory 
 PhD thesis , Radboud University Nijmegen , 2009 
 [ 24 ] Lawrence C
 Paulson 
 Set theory for verification : I 
 From foundations to functions 
 Journal of Automated Reasoning , 11 ( 3 ) :353–389 , 1993 
 [ 25 ] Lawrence C
 Paulson 
 The relative consistency of the axiom of choice — mechanized using Isabelle/ZF 
 LMS Journal of Computation and Mathematics , 6:198–248 , 2003
 http : //www
lms
ac
uk/jcm/6/lms2003-001/ 
 [ 26 ] Lawrence C
 Paulson 
 G¨odel ’ s incompleteness theorems 
 Archive of Formal Proofs , November 2013
 http : //afp
sf
net/entries/Incompleteness
shtml , Formal proof development 
 [ 27 ] Lawrence C
 Paulson 
 A machine-assisted proof of G¨odel ’ s incompleteness theorems for the theory of hereditarily finite sets 
 Review of Symbolic Logic , 7 ( 3 ) :484–498 , September 2014 
 [ 28 ] Andrew M
 Pitts 
 Nominal Sets : Names and Symmetry in Computer Science 
 Cambridge University Press , 2013 
 [ 29 ] Natarajan Shankar 
 Proof-checking Metamathematics 
 PhD thesis , University of Texas at Austin , 1986 
 [ 30 ] Natarajan Shankar 
 Metamathematics , Machines , and G¨odel ’ s Proof 
 Cambridge University Press , 1994 
 [ 31 ] Natarajan Shankar 
 Shankar , Boyer , Church-Rosser and de Bruijn indices 
 E-mail , 2013 
 38 [ 32 ] S
 Swierczkowski 
 Finite sets and G¨odel ’ s incompleteness th ´ eorems 
 Dissertationes Mathematicae , 422:1–58 , 2003
 http : //journals
impan
gov
pl/dm/Inf/422-0-1
html 
 [ 33 ] Christian Urban 
 Nominal techniques in Isabelle/HOL 
 Journal of Automated Reasoning , 40 ( 4 ) :327–356 , 2008 
 [ 34 ] Christian Urban and Cezary Kaliszyk 
 General bindings and alpha-equivalence in Nominal Isabelle 
 Logical Methods in Computer Science , 8 ( 2:14 ) :1–35 , 2012 


Introspector: INPUT:!@>Seeker:#80 Connor 
 Incompleteness & Completeness : Formalizing Logic and Analysis in Type Theory 
 PhD thesis , Radboud University Nijmegen , 2009 
 [ 24 ] Lawrence C
 Paulson 
 Set theory for verification : I 
 From foundations to functions 
 Journal of Automated Reasoning , 11 ( 3 ) :353–389 , 1993 
 [ 25 ] Lawrence C
 Paulson 
 The relative consistency of the axiom of choice — mechanized using Isabelle/ZF 
 LMS Journal of Computation and Mathematics , 6:198–248 , 2003
 http : //www
lms
ac
uk/jcm/6/lms2003-001/ 
 [ 26 ] Lawrence C
 Paulson 
 G¨odel ’ s incompleteness theorems 
 Archive of Formal Proofs , November 2013
 http : //afp
sf
net/entries/Incompleteness
shtml , Formal proof development 
 [ 27 ] Lawrence C
 Paulson 
 A machine-assisted proof of G¨odel ’ s incompleteness theorems for the theory of hereditarily finite sets 
 Review of Symbolic Logic , 7 ( 3 ) :484–498 , September 2014 
 [ 28 ] Andrew M
 Pitts 
 Nominal Sets : Names and Symmetry in Computer Science 
 Cambridge University Press , 2013 
 [ 29 ] Natarajan Shankar 
 Proof-checking Metamathematics 
 PhD thesis , University of Texas at Austin , 1986 
 [ 30 ] Natarajan Shankar 
 Metamathematics , Machines , and G¨odel ’ s Proof 
 Cambridge University Press , 1994 
 [ 31 ] Natarajan Shankar 
 Shankar , Boyer , Church-Rosser and de Bruijn indices 
 E-mail , 2013 
 38 [ 32 ] S
 Swierczkowski 
 Finite sets and G¨odel ’ s incompleteness th ´ eorems 
 Dissertationes Mathematicae , 422:1–58 , 2003
 http : //journals
impan
gov
pl/dm/Inf/422-0-1
html 
 [ 33 ] Christian Urban 
 Nominal techniques in Isabelle/HOL 
 Journal of Automated Reasoning , 40 ( 4 ) :327–356 , 2008 
 [ 34 ] Christian Urban and Cezary Kaliszyk 
 General bindings and alpha-equivalence in Nominal Isabelle 
 Logical Methods in Computer Science , 8 ( 2:14 ) :1–35 , 2012 


Here are some possible rewrites of the given text using poetic language and imagery:
* "Epic tale of formal reasoning! * @ > Seeker #80 Connor embarked on quest for truth, armed with logic's sharp sword and keen mind. His journey took him through realms of type theory, set theory, and more, where he encountered legends like Gdel and his famous incompleteness theorems."
* "A cosmic odyssey unfolds! ** @ > Seeker #80 Connor ventured into the vast expanse of mathematics, guided by stars of logic and analysis. He navigated treacherous seas of formal systems, braving tempests of inconsistency and uncertainty, until finally reaching shores of completeness and understanding."
* "An epic adventure through the labyrinthine world of mathematical thought! ** @ > Seeker #80 Connor delved deep into the mysteries of type theory and its ilk, uncovering hidden chambers filled with ancient wisdom and modern marvels alike. With each step forward, he discovered new secrets and insights that illuminated the path ahead..."
* "The seeker's pilgrimage continues...** @ > Seeker #80 Connor traversed mountains of metalogic, valleys of validation, and oceans of ontological wonderment. Through trials of time and space, he attained enlightenment from gurus of the field – Gdel among them - gaining profound insight into the nature of reality itself!"</s>Here are some possible rewrites of the given text using poetic language and imagery:
* "Epic tale of formal reasoning! * @ > Seeker #80 Connor embarked on quest for truth, armed with logic's sharp sword and keen mind. His journey took him through realms of type theory, set theory, and more, where he encountered legends like Gdel and his famous incompleteness theorems."
* "A cosmic odyssey unfolds! ** @ > Seeker #80 Connor ventured into the vast expanse of mathematics, guided by stars of logic and analysis. He navigated treacherous seas of formal systems, braving tempests of inconsistency and uncertainty, until finally reaching shores of completeness and understanding."
* "An epic adventure through the labyrinthine world of mathematical thought! ** @ > Seeker #80 Connor delved deep into the mysteries of type theory and its ilk, uncovering hidden chambers filled with ancient wisdom and modern marvels alike. With each step forward, he discovered new secrets and insights that illuminated the path ahead..."
* "The seeker's pilgrimage continues...** @ > Seeker #80 Connor traversed mountains of metalogic, valleys of validation, and oceans of ontological wonderment. Through trials of time and space, he attained enlightenment from gurus of the field – Gdel among them - gaining profound insight into the nature of reality


You: !@>Seeker:#81 
 General bindings and alpha-equivalence in Nominal Isabelle 
 Logical Methods in Computer Science , 8 ( 2:14 ) :1–35 , 2012 


Introspector: INPUT:!@>Seeker:#81 
 General bindings and alpha-equivalence in Nominal Isabelle 
 Logical Methods in Computer Science , 8 ( 2:14 ) :1–35 , 2012 


My rewritten version:
In realms beyond mortal sight, where syntax reigns supreme,
A tale unfolds 'midst code's celestial gleam;
Nominal Isabella, queen of logical grace,
With bindings tight, her kingdom holds its place...
The alpha-equivalent, an elusive dream,
Where reasoning rules, and truth doth beam...
Through trials fierce, she stood unshaken ground,
Her methods sharp, they pierced the clouded round...
And thus, within that hallowed nomadic space,
Alpha-equivalents found their proper pace!</s>My rewritten version:
In realms beyond mortal sight, where syntax reigns supreme,
A tale unfolds 'midst code's celestial gleam;
Nominal Isabella, queen of logical grace,
With bindings tight, her kingdom holds its place...
The alpha-equivalent, an elusive dream,
Where reasoning rules, and truth doth beam...
Through trials fierce, she stood unshaken ground,
Her methods sharp, they pierced the clouded round...
And thus, within that hallowed nomadic space,
Alpha-equivalents found their proper

