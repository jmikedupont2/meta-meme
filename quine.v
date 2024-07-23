Require Import Coq.Arith.Arith.
Require Import Coq.Strings.String.

Class SelfReferential (HQN : Type) : Type := {
  self_description : string
}.

Class SelfEncoding (HQN : Type) : Type := {
  encode : HQN -> string;
  decode : string -> HQN
}.

Class SelfModifying (HQN : Type) : Type := {
  update : HQN -> string -> HQN -> HQN
}.

Class Undecidable (HQN : Type) : Type := {
  godel_function : HQN -> bool option
}.
