export type ModelOption = {
  id: string;
  name: string;
  description: string;
}

export type CompileRequest = {
  spec: string;
  compilerModel: string;
  interpreterModel: string;
  inputExamples: string;
  outputExamples: string;
}

export type CompileResponse = {
  success: boolean;
  compiledModelId: string;
  downloadUrl: string;
  message?: string;
  error?: string;
}

export type TestRequest = {
  compiledModelId: string;
  input: string;
  generateTestData?: boolean;
}

export type TestResponse = {
  success: boolean;
  output: string;
  error?: string;
}

export type GenerateTestDataRequest = {
  spec: string;
  numExamples: number;
}

export type GenerateTestDataResponse = {
  success: boolean;
  examples: Array<{
    input: string;
    output: string;
  }>;
  error?: string;
}

// Program and voting types
export type Program = {
  id: string;
  title: string;
  description: string;
  specification: string;
  inputExamples: string;
  outputExamples: string;
  author: string;
  createdAt: string;
  updatedAt: string;
  votes: number;
  userVote?: 'up' | 'down' | null;
  tags: string[];
  compilerModel: string;
  interpreterModel: string;
  compiledModelId?: string;
  isPublic: boolean;
}

export type ProgramListResponse = {
  success: boolean;
  programs: Program[];
  totalCount: number;
  page: number;
  pageSize: number;
  error?: string;
}

export type ProgramDetailResponse = {
  success: boolean;
  program: Program;
  error?: string;
}

export type PublishProgramRequest = {
  title: string;
  description: string;
  specification: string;
  inputExamples: string;
  outputExamples: string;
  author: string;
  tags: string[];
  compilerModel: string;
  interpreterModel: string;
  compiledModelId?: string;
}

export type PublishProgramResponse = {
  success: boolean;
  program: Program;
  error?: string;
}

export type VoteRequest = {
  programId: string;
  voteType: 'up' | 'down' | 'remove';
}

export type VoteResponse = {
  success: boolean;
  newVoteCount: number;
  userVote: 'up' | 'down' | null;
  error?: string;
}
