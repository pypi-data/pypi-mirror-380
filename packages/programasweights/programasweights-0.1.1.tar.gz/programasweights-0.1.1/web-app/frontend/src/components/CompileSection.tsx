import React from 'react';
import { Play, Download, Loader } from 'lucide-react';

interface CompileSectionProps {
  onCompile: () => void;
  onDownload: () => void;
  compiling: boolean;
  compiled: boolean;
  canCompile: boolean;
}

const CompileSection: React.FC<CompileSectionProps> = ({
  onCompile,
  onDownload,
  compiling,
  compiled,
  canCompile
}) => {
  return (
    <div className="card p-6">
      <div className="flex items-center justify-between">
        <div>
          <h3 className="text-lg font-semibold text-gray-900 mb-2">Compile Program</h3>
          <p className="text-sm text-gray-600">
            Generate your neural program weights based on the specification and examples.
          </p>
        </div>
        
        <div className="flex items-center space-x-3">
          {compiled && (
            <button
              onClick={onDownload}
              className="btn-secondary flex items-center space-x-2"
            >
              <Download className="w-4 h-4" />
              <span>Download .tgz</span>
            </button>
          )}
          
          <button
            onClick={onCompile}
            disabled={!canCompile || compiling}
            className="btn-primary flex items-center space-x-2"
          >
            {compiling ? (
              <Loader className="w-4 h-4 animate-spin" />
            ) : (
              <Play className="w-4 h-4" />
            )}
            <span>{compiling ? 'Compiling...' : 'Compile'}</span>
          </button>
        </div>
      </div>
      
      {compiling && (
        <div className="mt-4 p-3 bg-blue-50 border border-blue-200 rounded-lg">
          <p className="text-sm text-blue-800">
            Compiling your program... This may take a few minutes.
          </p>
        </div>
      )}
      
      {compiled && (
        <div className="mt-4 p-3 bg-green-50 border border-green-200 rounded-lg">
          <p className="text-sm text-green-800">
            ✅ Program compiled successfully! You can now test it below or download the weights.
          </p>
        </div>
      )}
    </div>
  );
};

export default CompileSection;
