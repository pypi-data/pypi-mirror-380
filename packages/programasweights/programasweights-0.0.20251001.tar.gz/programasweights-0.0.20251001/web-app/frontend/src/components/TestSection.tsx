import React, { useState } from 'react';
import { Send, Wand2, Copy, Check } from 'lucide-react';

interface TestSectionProps {
  onTest: (input: string, generateTestData?: boolean) => void;
  testing: boolean;
  compiled: boolean;
  result: string;
}

const TestSection: React.FC<TestSectionProps> = ({
  onTest,
  testing,
  compiled,
  result
}) => {
  const [testInput, setTestInput] = useState('');
  const [copied, setCopied] = useState(false);

  const handleTest = (generateTestData = false) => {
    if (testInput.trim() || generateTestData) {
      onTest(testInput, generateTestData);
    }
  };

  const handleCopy = async () => {
    if (result) {
      await navigator.clipboard.writeText(result);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    }
  };

  if (!compiled) {
    return (
      <div className="card p-6 opacity-50">
        <h3 className="text-lg font-semibold text-gray-900 mb-2">Test Your Program</h3>
        <p className="text-sm text-gray-600">
          Compile your program first to enable testing.
        </p>
      </div>
    );
  }

  return (
    <div className="card p-6">
      <h3 className="text-lg font-semibold text-gray-900 mb-4">Test Your Program</h3>
      
      <div className="space-y-4">
        <div className="space-y-2">
          <label className="text-sm font-medium text-gray-700">Test Input</label>
          <div className="flex space-x-2">
            <textarea
              value={testInput}
              onChange={(e) => setTestInput(e.target.value)}
              placeholder="Enter test input..."
              rows={3}
              className="textarea-field flex-1"
            />
            <div className="flex flex-col space-y-2">
              <button
                onClick={() => handleTest(false)}
                disabled={testing || !testInput.trim()}
                className="btn-primary flex items-center space-x-1 whitespace-nowrap"
              >
                <Send className="w-4 h-4" />
                <span>Test</span>
              </button>
              <button
                onClick={() => handleTest(true)}
                disabled={testing}
                className="btn-secondary flex items-center space-x-1 whitespace-nowrap"
              >
                <Wand2 className="w-4 h-4" />
                <span>Generate & Test</span>
              </button>
            </div>
          </div>
        </div>
        
        {result && (
          <div className="space-y-2">
            <div className="flex items-center justify-between">
              <label className="text-sm font-medium text-gray-700">Output</label>
              <button
                onClick={handleCopy}
                className="flex items-center space-x-1 text-xs text-gray-500 hover:text-gray-700 transition-colors"
              >
                {copied ? (
                  <>
                    <Check className="w-3 h-3" />
                    <span>Copied!</span>
                  </>
                ) : (
                  <>
                    <Copy className="w-3 h-3" />
                    <span>Copy</span>
                  </>
                )}
              </button>
            </div>
            <div className="bg-gray-50 border border-gray-200 rounded-lg p-3">
              <pre className="text-sm text-gray-800 whitespace-pre-wrap font-mono">
                {result}
              </pre>
            </div>
          </div>
        )}
        
        {testing && (
          <div className="p-3 bg-blue-50 border border-blue-200 rounded-lg">
            <p className="text-sm text-blue-800">
              Running your program...
            </p>
          </div>
        )}
      </div>
    </div>
  );
};

export default TestSection;
