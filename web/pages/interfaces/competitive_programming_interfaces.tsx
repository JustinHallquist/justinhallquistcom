export interface ProblemContent {
  problem: string;
  problem_in: string;
  problem_out: string;
  problem_supplement: string;
  solution: string;
  explanation: string;
}

export interface Content {
  [index: string]: ProblemContent
}

