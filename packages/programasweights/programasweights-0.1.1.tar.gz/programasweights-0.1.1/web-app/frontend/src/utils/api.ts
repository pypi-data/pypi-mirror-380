import axios from 'axios';
import type { 
  ModelOption, 
  CompileRequest, 
  CompileResponse, 
  TestRequest, 
  TestResponse, 
  GenerateTestDataRequest, 
  GenerateTestDataResponse,
  ProgramListResponse,
  ProgramDetailResponse,
  PublishProgramRequest,
  PublishProgramResponse,
  VoteRequest,
  VoteResponse
} from '../types';

const API_BASE_URL = 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const apiClient = {
  // Get available models
  getCompilerModels: async (): Promise<ModelOption[]> => {
    const response = await api.get('/models/compiler');
    return response.data;
  },

  getInterpreterModels: async (): Promise<ModelOption[]> => {
    const response = await api.get('/models/interpreter');
    return response.data;
  },

  // Compile spec to model
  compileModel: async (request: CompileRequest): Promise<CompileResponse> => {
    const response = await api.post('/compile', request);
    return response.data;
  },

  // Test compiled model
  testModel: async (request: TestRequest): Promise<TestResponse> => {
    const response = await api.post('/test', request);
    return response.data;
  },

  // Generate test data using GPT
  generateTestData: async (request: GenerateTestDataRequest): Promise<GenerateTestDataResponse> => {
    const response = await api.post('/generate-test-data', request);
    return response.data;
  },

  // Download compiled model
  downloadModel: async (compiledModelId: string): Promise<Blob> => {
    const response = await api.get(`/download/${compiledModelId}`, {
      responseType: 'blob',
    });
    return response.data;
  },

  // Program management
  getPrograms: async (page: number = 1, pageSize: number = 20, sortBy: string = 'votes'): Promise<ProgramListResponse> => {
    const response = await api.get(`/programs?page=${page}&pageSize=${pageSize}&sortBy=${sortBy}`);
    return response.data;
  },

  getProgram: async (programId: string): Promise<ProgramDetailResponse> => {
    const response = await api.get(`/programs/${programId}`);
    return response.data;
  },

  publishProgram: async (request: PublishProgramRequest): Promise<PublishProgramResponse> => {
    const response = await api.post('/programs', request);
    return response.data;
  },

  voteProgram: async (request: VoteRequest): Promise<VoteResponse> => {
    const response = await api.post('/programs/vote', request);
    return response.data;
  },
};

export default apiClient;
