import React, { useState, useEffect } from 'react';
import toast from 'react-hot-toast';
import ModelSelector from './ModelSelector';
import SpecInput from './SpecInput';
import ExamplesInput from './ExamplesInput';
import CompileSection from './CompileSection';
import TestSection from './TestSection';
import { apiClient } from '../utils/api';

interface ModelOption {
  id: string;
  name: string;
  description: string;
}

const MainInterface: React.FC = () => {
  // Model options
  const [compilerModels, setCompilerModels] = useState<ModelOption[]>([]);
  const [interpreterModels, setInterpreterModels] = useState<ModelOption[]>([]);
  const [loadingModels, setLoadingModels] = useState(true);

  // Form state
  const [compilerModel, setCompilerModel] = useState('');
  const [interpreterModel, setInterpreterModel] = useState('');
  const [spec, setSpec] = useState('');
  const [inputExamples, setInputExamples] = useState('');
  const [outputExamples, setOutputExamples] = useState('');

  // Compilation state
  const [compiling, setCompiling] = useState(false);
  const [compiled, setCompiled] = useState(false);
  const [compiledModelId, setCompiledModelId] = useState('');

  // Testing state
  const [testing, setTesting] = useState(false);
  const [testResult, setTestResult] = useState('');

  // Other states
  const [generatingExamples, setGeneratingExamples] = useState(false);

  // Load available models on component mount
  useEffect(() => {
    const loadModels = async () => {
      try {
        const [compilerOpts, interpreterOpts] = await Promise.all([
          apiClient.getCompilerModels(),
          apiClient.getInterpreterModels()
        ]);
        
        setCompilerModels(compilerOpts);
        setInterpreterModels(interpreterOpts);
        
        // Set default selections
        if (compilerOpts.length > 0) {
          setCompilerModel(compilerOpts[0].id);
        }
        if (interpreterOpts.length > 0) {
          setInterpreterModel(interpreterOpts[0].id);
        }
      } catch (error) {
        toast.error('Failed to load available models');
        console.error('Error loading models:', error);
      } finally {
        setLoadingModels(false);
      }
    };

    loadModels();
  }, []);

  const handleGenerateExamples = async () => {
    if (!spec.trim()) {
      toast.error('Please enter a program specification first');
      return;
    }

    setGeneratingExamples(true);
    try {
      const response = await apiClient.generateTestData({
        spec,
        numExamples: 5
      });

      if (response.success) {
        const inputs = response.examples.map(ex => ex.input).join('\n');
        const outputs = response.examples.map(ex => ex.output).join('\n');
        
        setInputExamples(inputs);
        setOutputExamples(outputs);
        toast.success('Generated example data successfully!');
      } else {
        toast.error(response.error || 'Failed to generate examples');
      }
    } catch (error) {
      toast.error('Error generating examples');
      console.error('Error generating examples:', error);
    } finally {
      setGeneratingExamples(false);
    }
  };

  const handleCompile = async () => {
    if (!spec.trim()) {
      toast.error('Please enter a program specification');
      return;
    }
    if (!compilerModel || !interpreterModel) {
      toast.error('Please select both compiler and interpreter models');
      return;
    }

    setCompiling(true);
    setCompiled(false);
    setTestResult('');
    
    try {
      const response = await apiClient.compileModel({
        spec,
        compilerModel,
        interpreterModel,
        inputExamples,
        outputExamples
      });

      if (response.success) {
        setCompiled(true);
        setCompiledModelId(response.compiledModelId);
        toast.success('Program compiled successfully!');
      } else {
        toast.error(response.error || 'Compilation failed');
      }
    } catch (error) {
      toast.error('Error during compilation');
      console.error('Compilation error:', error);
    } finally {
      setCompiling(false);
    }
  };

  const handleDownload = async () => {
    if (!compiledModelId) return;

    try {
      const blob = await apiClient.downloadModel(compiledModelId);
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.style.display = 'none';
      a.href = url;
      a.download = `${compiledModelId}.tgz`;
      document.body.appendChild(a);
      a.click();
      window.URL.revokeObjectURL(url);
      document.body.removeChild(a);
      toast.success('Download started!');
    } catch (error) {
      toast.error('Error downloading model');
      console.error('Download error:', error);
    }
  };

  const handleTest = async (input: string, generateTestData = false) => {
    if (!compiledModelId) return;

    setTesting(true);
    try {
      const response = await apiClient.testModel({
        compiledModelId,
        input,
        generateTestData
      });

      if (response.success) {
        setTestResult(response.output);
      } else {
        toast.error(response.error || 'Test failed');
        setTestResult('');
      }
    } catch (error) {
      toast.error('Error testing model');
      console.error('Test error:', error);
      setTestResult('');
    } finally {
      setTesting(false);
    }
  };

  const canCompile = spec.trim() && compilerModel && interpreterModel && !loadingModels;

  return (
    <div className="max-w-6xl mx-auto space-y-8">
      {/* Model Selection */}
      <div className="card p-6">
        <h2 className="text-xl font-bold text-gray-900 mb-6">Model Configuration</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <ModelSelector
            label="Compiler Model"
            options={compilerModels}
            value={compilerModel}
            onChange={setCompilerModel}
            loading={loadingModels}
            placeholder="Select compiler model..."
          />
          <ModelSelector
            label="Interpreter Model"
            options={interpreterModels}
            value={interpreterModel}
            onChange={setInterpreterModel}
            loading={loadingModels}
            placeholder="Select interpreter model..."
          />
        </div>
      </div>

      {/* Program Specification */}
      <SpecInput
        value={spec}
        onChange={setSpec}
        placeholder="Parse a string like '(A) ... (B) ... (C) ...' into a JSON list of options. Be robust to noise: extra spaces, bullets, and phrases like 'both (A) and (B)'."
      />

      {/* Input/Output Examples */}
      <ExamplesInput
        inputExamples={inputExamples}
        outputExamples={outputExamples}
        onInputExamplesChange={setInputExamples}
        onOutputExamplesChange={setOutputExamples}
        onGenerateExamples={handleGenerateExamples}
        generatingExamples={generatingExamples}
      />

      {/* Compile Section */}
      <CompileSection
        onCompile={handleCompile}
        onDownload={handleDownload}
        compiling={compiling}
        compiled={compiled}
        canCompile={canCompile}
      />

      {/* Test Section */}
      <TestSection
        onTest={handleTest}
        testing={testing}
        compiled={compiled}
        result={testResult}
      />
    </div>
  );
};

export default MainInterface;
