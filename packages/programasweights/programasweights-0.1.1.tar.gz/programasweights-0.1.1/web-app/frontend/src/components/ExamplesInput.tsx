import React from 'react';
import { Lightbulb, Wand2 } from 'lucide-react';

interface ExamplesInputProps {
  inputExamples: string;
  outputExamples: string;
  onInputExamplesChange: (value: string) => void;
  onOutputExamplesChange: (value: string) => void;
  onGenerateExamples: () => void;
  generatingExamples: boolean;
}

const ExamplesInput: React.FC<ExamplesInputProps> = ({
  inputExamples,
  outputExamples,
  onInputExamplesChange,
  onOutputExamplesChange,
  onGenerateExamples,
  generatingExamples
}) => {
  return (
    <div className="card p-6">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center space-x-2">
          <Lightbulb className="w-5 h-5 text-primary-600" />
          <h3 className="text-lg font-semibold text-gray-900">Input/Output Examples</h3>
        </div>
        <button
          onClick={onGenerateExamples}
          disabled={generatingExamples}
          className="btn-secondary flex items-center space-x-2 text-sm"
        >
          <Wand2 className="w-4 h-4" />
          <span>{generatingExamples ? 'Generating...' : 'Generate with GPT'}</span>
        </button>
      </div>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="space-y-2">
          <label className="text-sm font-medium text-gray-700">
            Input Examples
          </label>
          <textarea
            value={inputExamples}
            onChange={(e) => onInputExamplesChange(e.target.value)}
            placeholder="Example inputs (one per line)..."
            rows={8}
            className="textarea-field"
          />
        </div>
        
        <div className="space-y-2">
          <label className="text-sm font-medium text-gray-700">
            Expected Output Examples
          </label>
          <textarea
            value={outputExamples}
            onChange={(e) => onOutputExamplesChange(e.target.value)}
            placeholder="Expected outputs (one per line, corresponding to inputs)..."
            rows={8}
            className="textarea-field"
          />
        </div>
      </div>
      
      <p className="text-xs text-gray-500 mt-3">
        Provide example inputs and their expected outputs to help train your program. 
        You can manually enter them or use GPT to generate examples based on your specification.
      </p>
    </div>
  );
};

export default ExamplesInput;
