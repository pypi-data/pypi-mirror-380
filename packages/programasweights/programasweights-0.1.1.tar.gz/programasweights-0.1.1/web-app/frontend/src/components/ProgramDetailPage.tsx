import { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { 
  ChevronUp, 
  ChevronDown, 
  ArrowLeft, 
  Calendar, 
  User, 
  Tag, 
  Download,
  Play,
  Copy,
  Check,
  Code,
  FileText,
  Settings
} from 'lucide-react';
import type { Program, ProgramDetailResponse, TestRequest, TestResponse } from '../types';
import { apiClient } from '../utils/api';
import toast from 'react-hot-toast';

const ProgramDetailPage: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const [program, setProgram] = useState<Program | null>(null);
  const [loading, setLoading] = useState(true);
  const [testInput, setTestInput] = useState('');
  const [testOutput, setTestOutput] = useState('');
  const [testLoading, setTestLoading] = useState(false);
  const [copiedSpec, setCopiedSpec] = useState(false);
  const [copiedInput, setCopiedInput] = useState(false);
  const [copiedOutput, setCopiedOutput] = useState(false);

  useEffect(() => {
    if (id) {
      loadProgram(id);
    }
  }, [id]);

  const loadProgram = async (programId: string) => {
    try {
      setLoading(true);
      const response: ProgramDetailResponse = await apiClient.getProgram(programId);
      
      if (response.success) {
        setProgram(response.program);
      } else {
        toast.error(response.error || 'Failed to load program');
      }
    } catch (error) {
      toast.error('Failed to load program');
      console.error('Error loading program:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleVote = async (voteType: 'up' | 'down') => {
    if (!program) return;

    try {
      const response = await apiClient.voteProgram({ programId: program.id, voteType });
      
      if (response.success) {
        setProgram(prev => prev ? {
          ...prev,
          votes: response.newVoteCount,
          userVote: response.userVote
        } : null);
        toast.success(`Vote ${voteType === 'up' ? 'up' : 'down'} recorded!`);
      } else {
        toast.error(response.error || 'Failed to vote');
      }
    } catch (error) {
      toast.error('Failed to vote');
      console.error('Error voting:', error);
    }
  };

  const handleTest = async () => {
    if (!program || !program.compiledModelId || !testInput.trim()) return;

    try {
      setTestLoading(true);
      const testRequest: TestRequest = {
        compiledModelId: program.compiledModelId,
        input: testInput
      };

      const response: TestResponse = await apiClient.testModel(testRequest);
      
      if (response.success) {
        setTestOutput(response.output);
        toast.success('Test completed successfully!');
      } else {
        toast.error(response.error || 'Test failed');
        setTestOutput('');
      }
    } catch (error) {
      toast.error('Failed to run test');
      console.error('Error testing program:', error);
    } finally {
      setTestLoading(false);
    }
  };

  const handleDownload = async () => {
    if (!program || !program.compiledModelId) return;

    try {
      const blob = await apiClient.downloadModel(program.compiledModelId);
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `${program.title.replace(/\s+/g, '_')}.tgz`;
      document.body.appendChild(a);
      a.click();
      window.URL.revokeObjectURL(url);
      document.body.removeChild(a);
      toast.success('Download started!');
    } catch (error) {
      toast.error('Failed to download model');
      console.error('Error downloading model:', error);
    }
  };

  const copyToClipboard = async (text: string, type: 'spec' | 'input' | 'output') => {
    try {
      await navigator.clipboard.writeText(text);
      
      if (type === 'spec') setCopiedSpec(true);
      else if (type === 'input') setCopiedInput(true);
      else setCopiedOutput(true);

      setTimeout(() => {
        setCopiedSpec(false);
        setCopiedInput(false);
        setCopiedOutput(false);
      }, 2000);

      toast.success('Copied to clipboard!');
    } catch (error) {
      toast.error('Failed to copy to clipboard');
    }
  };

  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
      </div>
    );
  }

  if (!program) {
    return (
      <div className="text-center py-12">
        <h2 className="text-2xl font-bold text-gray-900 mb-4">Program Not Found</h2>
        <p className="text-gray-600 mb-6">The requested program could not be found.</p>
        <Link
          to="/leaderboard"
          className="inline-flex items-center px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
        >
          <ArrowLeft className="w-4 h-4 mr-2" />
          Back to Leaderboard
        </Link>
      </div>
    );
  }

  return (
    <div className="max-w-4xl mx-auto">
      {/* Back Button */}
      <Link
        to="/leaderboard"
        className="inline-flex items-center text-gray-600 hover:text-gray-900 mb-6 transition-colors"
      >
        <ArrowLeft className="w-4 h-4 mr-2" />
        Back to Leaderboard
      </Link>

      {/* Header */}
      <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6 mb-6">
        <div className="flex items-start gap-6">
          {/* Voting */}
          <div className="flex flex-col items-center">
            <button
              onClick={() => handleVote('up')}
              className={`p-2 rounded-md transition-colors ${
                program.userVote === 'up'
                  ? 'text-green-600 bg-green-100'
                  : 'text-gray-400 hover:text-green-600 hover:bg-green-50'
              }`}
            >
              <ChevronUp className="w-6 h-6" />
            </button>
            <span className="text-lg font-bold text-gray-900 py-2">
              {program.votes}
            </span>
            <button
              onClick={() => handleVote('down')}
              className={`p-2 rounded-md transition-colors ${
                program.userVote === 'down'
                  ? 'text-red-600 bg-red-100'
                  : 'text-gray-400 hover:text-red-600 hover:bg-red-50'
              }`}
            >
              <ChevronDown className="w-6 h-6" />
            </button>
          </div>

          {/* Program Info */}
          <div className="flex-1">
            <h1 className="text-3xl font-bold text-gray-900 mb-4">{program.title}</h1>
            <p className="text-gray-700 text-lg mb-4">{program.description}</p>
            
            <div className="flex flex-wrap items-center gap-6 text-sm text-gray-600 mb-4">
              <div className="flex items-center gap-2">
                <User className="w-4 h-4" />
                <span className="font-medium">By {program.author}</span>
              </div>
              <div className="flex items-center gap-2">
                <Calendar className="w-4 h-4" />
                <span>Created {formatDate(program.createdAt)}</span>
              </div>
              {program.updatedAt !== program.createdAt && (
                <div className="flex items-center gap-2">
                  <Calendar className="w-4 h-4" />
                  <span>Updated {formatDate(program.updatedAt)}</span>
                </div>
              )}
            </div>

            {/* Tags */}
            {program.tags.length > 0 && (
              <div className="flex items-center gap-2 mb-4">
                <Tag className="w-4 h-4 text-gray-400" />
                <div className="flex flex-wrap gap-2">
                  {program.tags.map(tag => (
                    <span
                      key={tag}
                      className="px-3 py-1 bg-blue-100 text-blue-800 rounded-full text-sm font-medium"
                    >
                      {tag}
                    </span>
                  ))}
                </div>
              </div>
            )}

            {/* Actions */}
            <div className="flex gap-3">
              {program.compiledModelId && (
                <button
                  onClick={handleDownload}
                  className="inline-flex items-center px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
                >
                  <Download className="w-4 h-4 mr-2" />
                  Download Model
                </button>
              )}
              <Link
                to="/publish"
                state={{ fromProgram: program }}
                className="inline-flex items-center px-4 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 transition-colors"
              >
                <Code className="w-4 h-4 mr-2" />
                Fork Program
              </Link>
            </div>
          </div>
        </div>
      </div>

      {/* Program Details */}
      <div className="grid lg:grid-cols-2 gap-6 mb-6">
        {/* Specification */}
        <div className="bg-white rounded-lg shadow-sm border border-gray-200">
          <div className="p-4 border-b border-gray-200">
            <div className="flex items-center justify-between">
              <h3 className="text-lg font-semibold text-gray-900 flex items-center">
                <FileText className="w-5 h-5 mr-2" />
                Specification
              </h3>
              <button
                onClick={() => copyToClipboard(program.specification, 'spec')}
                className="p-2 text-gray-400 hover:text-gray-600 transition-colors"
              >
                {copiedSpec ? <Check className="w-4 h-4 text-green-600" /> : <Copy className="w-4 h-4" />}
              </button>
            </div>
          </div>
          <div className="p-4">
            <pre className="whitespace-pre-wrap text-sm text-gray-800 bg-gray-50 p-4 rounded-lg overflow-auto max-h-64">
              {program.specification}
            </pre>
          </div>
        </div>

        {/* Model Configuration */}
        <div className="bg-white rounded-lg shadow-sm border border-gray-200">
          <div className="p-4 border-b border-gray-200">
            <h3 className="text-lg font-semibold text-gray-900 flex items-center">
              <Settings className="w-5 h-5 mr-2" />
              Model Configuration
            </h3>
          </div>
          <div className="p-4 space-y-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Compiler Model
              </label>
              <p className="text-sm text-gray-900 bg-gray-50 p-2 rounded">
                {program.compilerModel}
              </p>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Interpreter Model
              </label>
              <p className="text-sm text-gray-900 bg-gray-50 p-2 rounded">
                {program.interpreterModel}
              </p>
            </div>
            {program.compiledModelId && (
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Compiled Model ID
                </label>
                <p className="text-sm text-gray-900 bg-gray-50 p-2 rounded font-mono">
                  {program.compiledModelId}
                </p>
              </div>
            )}
          </div>
        </div>
      </div>

      {/* Examples */}
      <div className="grid lg:grid-cols-2 gap-6 mb-6">
        {/* Input Examples */}
        <div className="bg-white rounded-lg shadow-sm border border-gray-200">
          <div className="p-4 border-b border-gray-200">
            <div className="flex items-center justify-between">
              <h3 className="text-lg font-semibold text-gray-900">Input Examples</h3>
              <button
                onClick={() => copyToClipboard(program.inputExamples, 'input')}
                className="p-2 text-gray-400 hover:text-gray-600 transition-colors"
              >
                {copiedInput ? <Check className="w-4 h-4 text-green-600" /> : <Copy className="w-4 h-4" />}
              </button>
            </div>
          </div>
          <div className="p-4">
            <pre className="whitespace-pre-wrap text-sm text-gray-800 bg-gray-50 p-4 rounded-lg overflow-auto max-h-64">
              {program.inputExamples}
            </pre>
          </div>
        </div>

        {/* Output Examples */}
        <div className="bg-white rounded-lg shadow-sm border border-gray-200">
          <div className="p-4 border-b border-gray-200">
            <div className="flex items-center justify-between">
              <h3 className="text-lg font-semibold text-gray-900">Output Examples</h3>
              <button
                onClick={() => copyToClipboard(program.outputExamples, 'output')}
                className="p-2 text-gray-400 hover:text-gray-600 transition-colors"
              >
                {copiedOutput ? <Check className="w-4 h-4 text-green-600" /> : <Copy className="w-4 h-4" />}
              </button>
            </div>
          </div>
          <div className="p-4">
            <pre className="whitespace-pre-wrap text-sm text-gray-800 bg-gray-50 p-4 rounded-lg overflow-auto max-h-64">
              {program.outputExamples}
            </pre>
          </div>
        </div>
      </div>

      {/* Test Section */}
      {program.compiledModelId && (
        <div className="bg-white rounded-lg shadow-sm border border-gray-200">
          <div className="p-4 border-b border-gray-200">
            <h3 className="text-lg font-semibold text-gray-900 flex items-center">
              <Play className="w-5 h-5 mr-2" />
              Test This Program
            </h3>
          </div>
          <div className="p-4">
            <div className="grid lg:grid-cols-2 gap-6">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Test Input
                </label>
                <textarea
                  className="w-full h-32 px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none"
                  placeholder="Enter your test input here..."
                  value={testInput}
                  onChange={(e) => setTestInput(e.target.value)}
                />
                <button
                  onClick={handleTest}
                  disabled={testLoading || !testInput.trim()}
                  className="mt-3 w-full px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors flex items-center justify-center"
                >
                  {testLoading ? (
                    <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white mr-2"></div>
                  ) : (
                    <Play className="w-4 h-4 mr-2" />
                  )}
                  {testLoading ? 'Running...' : 'Run Test'}
                </button>
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Test Output
                </label>
                <div className="w-full h-32 px-3 py-2 border border-gray-300 rounded-lg bg-gray-50 overflow-auto">
                  {testOutput ? (
                    <pre className="whitespace-pre-wrap text-sm text-gray-900">
                      {testOutput}
                    </pre>
                  ) : (
                    <p className="text-gray-500 text-sm">
                      Output will appear here after running a test
                    </p>
                  )}
                </div>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default ProgramDetailPage;
