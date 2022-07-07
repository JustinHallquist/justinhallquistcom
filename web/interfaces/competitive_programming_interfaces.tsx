export interface ProblemContent {
  problem: string;
  problem_supplement: string;
  solution: string;
  explanation: string;
}

export interface Content {
  [index: string]: ProblemContent
}

