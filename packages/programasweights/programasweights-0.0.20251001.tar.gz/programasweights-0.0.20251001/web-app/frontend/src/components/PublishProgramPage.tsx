import { useState, useEffect } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { 
  Plus, 
  Save, 
  User, 
  FileText, 
  Tag, 
  Settings,
  AlertCircle,
  CheckCircle,
  Code,
  Play
} from 'lucide-react';
import type { 
  PublishProgramRequest, 
  PublishProgramResponse, 
  ModelOption,
  CompileRequest,
  CompileResponse
} from '../types';
import { apiClient } from '../utils/api';
import toast from 'react-hot-toast';

const PublishProgramPage: React.FC = () => {
  const location = useLocation();
  const navigate = useNavigate();
  
  // Form state
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [specification, setSpecification] = useState('');
  const [inputExamples, setInputExamples] = useState('');
  const [outputExamples, setOutputExamples] = useState('');
  const [author, setAuthor] = useState('');
  const [tags, setTags] = useState<string[]>([]);
  const [tagInput, setTagInput] = useState('');
  const [compilerModel, setCompilerModel] = useState('');
  const [interpreterModel, setInterpreterModel] = useState('');
  
  // Available models
  const [compilerModels, setCompilerModels] = useState<ModelOption[]>([]);
  const [interpreterModels, setInterpreterModels] = useState<ModelOption[]>([]);
  
  // Compilation state
  const [compiledModelId, setCompiledModelId] = useState<string>('');
  const [compiling, setCompiling] = useState(false);
  const [compiled, setCompiled] = useState(false);
  
  // Publishing state
  const [publishing, setPublishing] = useState(false);

  useEffect(() => {
    loadModels();
    
    // Pre-fill from existing program if forking
    const fromProgram = location.state?.fromProgram;
    if (fromProgram) {
      setTitle(`${fromProgram.title} (Fork)`);
      setDescription(fromProgram.description);
      setSpecification(fromProgram.specification);
      setInputExamples(fromProgram.inputExamples);
      setOutputExamples(fromProgram.outputExamples);
      setTags(fromProgram.tags);
      setCompilerModel(fromProgram.compilerModel);
      setInterpreterModel(fromProgram.interpreterModel);
    }
  }, [location.state]);

  const loadModels = async () => {
    try {
      const [compilerResponse, interpreterResponse] = await Promise.all([
        apiClient.getCompilerModels(),
        apiClient.getInterpreterModels()
      ]);
      
      setCompilerModels(compilerResponse);
      setInterpreterModels(interpreterResponse);
      
      // Set default models
      if (compilerResponse.length > 0 && !compilerModel) {
        setCompilerModel(compilerResponse[0].id);
      }
      if (interpreterResponse.length > 0 && !interpreterModel) {
        setInterpreterModel(interpreterResponse[0].id);
      }
    } catch (error) {
      toast.error('Failed to load available models');
      console.error('Error loading models:', error);
    }
  };

  const handleAddTag = () => {
    if (tagInput.trim() && !tags.includes(tagInput.trim())) {
      setTags([...tags, tagInput.trim()]);
      setTagInput('');
    }
  };

  const handleRemoveTag = (tagToRemove: string) => {
    setTags(tags.filter(tag => tag !== tagToRemove));
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      handleAddTag();
    }
  };

  const handleCompile = async () => {
    if (!specification.trim() || !compilerModel || !interpreterModel) {
      toast.error('Please fill in all required fields before compiling');
      return;
    }

    try {
      setCompiling(true);
      const compileRequest: CompileRequest = {
        spec: specification,
        compilerModel,
        interpreterModel,
        inputExamples,
        outputExamples
      };

      const response: CompileResponse = await apiClient.compileModel(compileRequest);
      
      if (response.success) {
        setCompiledModelId(response.compiledModelId);
        setCompiled(true);
        toast.success('Program compiled successfully! You can now publish it.');
      } else {
        toast.error(response.error || 'Compilation failed');
      }
    } catch (error) {
      toast.error('Failed to compile program');
      console.error('Error compiling program:', error);
    } finally {
      setCompiling(false);
    }
  };

  const handlePublish = async () => {
    if (!title.trim() || !description.trim() || !author.trim()) {
      toast.error('Please fill in all required fields');
      return;
    }

    try {
      setPublishing(true);
      const publishRequest: PublishProgramRequest = {
        title: title.trim(),
        description: description.trim(),
        specification,
        inputExamples,
        outputExamples,
        author: author.trim(),
        tags,
        compilerModel,
        interpreterModel,
        compiledModelId: compiled ? compiledModelId : undefined
      };

      const response: PublishProgramResponse = await apiClient.publishProgram(publishRequest);
      
      if (response.success) {
        toast.success('Program published successfully!');
        navigate(`/program/${response.program.id}`);
      } else {
        toast.error(response.error || 'Failed to publish program');
      }
    } catch (error) {
      toast.error('Failed to publish program');
      console.error('Error publishing program:', error);
    } finally {
      setPublishing(false);
    }
  };

  const isFormValid = title.trim() && description.trim() && specification.trim() && author.trim() && compilerModel && interpreterModel;

  return (
    <div className="max-w-4xl mx-auto">
      {/* Header */}
      <div className="text-center mb-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-4 flex items-center justify-center">
          <Plus className="w-8 h-8 mr-3 text-blue-600" />
          Publish Neural Program
        </h1>
        <p className="text-gray-600">
          Share your neural program with the community and contribute to the leaderboard
        </p>
      </div>

      <div className="grid lg:grid-cols-3 gap-6">
        {/* Main Form */}
        <div className="lg:col-span-2 space-y-6">
          {/* Basic Info */}
          <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
            <h2 className="text-xl font-semibold text-gray-900 mb-4 flex items-center">
              <FileText className="w-5 h-5 mr-2" />
              Basic Information
            </h2>
            
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Program Title *
                </label>
                <input
                  type="text"
                  className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  placeholder="Give your program a descriptive title"
                  value={title}
                  onChange={(e) => setTitle(e.target.value)}
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Description *
                </label>
                <textarea
                  className="w-full h-24 px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none"
                  placeholder="Describe what your program does and its use cases"
                  value={description}
                  onChange={(e) => setDescription(e.target.value)}
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Author *
                </label>
                <input
                  type="text"
                  className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  placeholder="Your name or username"
                  value={author}
                  onChange={(e) => setAuthor(e.target.value)}
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Tags
                </label>
                <div className="flex gap-2 mb-2">
                  <input
                    type="text"
                    className="flex-1 px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                    placeholder="Add tags (press Enter)"
                    value={tagInput}
                    onChange={(e) => setTagInput(e.target.value)}
                    onKeyPress={handleKeyPress}
                  />
                  <button
                    type="button"
                    onClick={handleAddTag}
                    className="px-4 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 transition-colors"
                  >
                    Add
                  </button>
                </div>
                {tags.length > 0 && (
                  <div className="flex flex-wrap gap-2">
                    {tags.map(tag => (
                      <span
                        key={tag}
                        className="inline-flex items-center px-3 py-1 bg-blue-100 text-blue-800 rounded-full text-sm"
                      >
                        <Tag className="w-3 h-3 mr-1" />
                        {tag}
                        <button
                          onClick={() => handleRemoveTag(tag)}
                          className="ml-2 text-blue-600 hover:text-blue-800"
                        >
                          ×
                        </button>
                      </span>
                    ))}
                  </div>
                )}
              </div>
            </div>
          </div>

          {/* Program Specification */}
          <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
            <h2 className="text-xl font-semibold text-gray-900 mb-4 flex items-center">
              <Code className="w-5 h-5 mr-2" />
              Program Specification
            </h2>
            
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Natural Language Specification *
                </label>
                <textarea
                  className="w-full h-32 px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none"
                  placeholder="Describe what your program should do in natural language..."
                  value={specification}
                  onChange={(e) => setSpecification(e.target.value)}
                />
              </div>

              <div className="grid md:grid-cols-2 gap-4">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Input Examples
                  </label>
                  <textarea
                    className="w-full h-32 px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none"
                    placeholder="Provide example inputs (one per line)"
                    value={inputExamples}
                    onChange={(e) => setInputExamples(e.target.value)}
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Output Examples
                  </label>
                  <textarea
                    className="w-full h-32 px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none"
                    placeholder="Provide corresponding outputs (one per line)"
                    value={outputExamples}
                    onChange={(e) => setOutputExamples(e.target.value)}
                  />
                </div>
              </div>
            </div>
          </div>

          {/* Model Configuration */}
          <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
            <h2 className="text-xl font-semibold text-gray-900 mb-4 flex items-center">
              <Settings className="w-5 h-5 mr-2" />
              Model Configuration
            </h2>
            
            <div className="grid md:grid-cols-2 gap-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Compiler Model *
                </label>
                <select
                  className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  value={compilerModel}
                  onChange={(e) => setCompilerModel(e.target.value)}
                >
                  <option value="">Select compiler model</option>
                  {compilerModels.map(model => (
                    <option key={model.id} value={model.id}>
                      {model.name}
                    </option>
                  ))}
                </select>
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Interpreter Model *
                </label>
                <select
                  className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  value={interpreterModel}
                  onChange={(e) => setInterpreterModel(e.target.value)}
                >
                  <option value="">Select interpreter model</option>
                  {interpreterModels.map(model => (
                    <option key={model.id} value={model.id}>
                      {model.name}
                    </option>
                  ))}
                </select>
              </div>
            </div>
          </div>
        </div>

        {/* Sidebar */}
        <div className="space-y-6">
          {/* Compilation Status */}
          <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
            <h3 className="text-lg font-semibold text-gray-900 mb-4">Compilation</h3>
            
            {!compiled ? (
              <div className="space-y-4">
                <div className="flex items-center text-amber-600">
                  <AlertCircle className="w-5 h-5 mr-2" />
                  <span className="text-sm">Not compiled yet</span>
                </div>
                <p className="text-sm text-gray-600">
                  Compile your program to test it and make it executable for others.
                </p>
                <button
                  onClick={handleCompile}
                  disabled={compiling || !specification.trim() || !compilerModel || !interpreterModel}
                  className="w-full px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors flex items-center justify-center"
                >
                  {compiling ? (
                    <>
                      <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white mr-2"></div>
                      Compiling...
                    </>
                  ) : (
                    <>
                      <Play className="w-4 h-4 mr-2" />
                      Compile Program
                    </>
                  )}
                </button>
              </div>
            ) : (
              <div className="space-y-4">
                <div className="flex items-center text-green-600">
                  <CheckCircle className="w-5 h-5 mr-2" />
                  <span className="text-sm">Successfully compiled</span>
                </div>
                <p className="text-sm text-gray-600">
                  Your program is ready to publish and can be executed by others.
                </p>
                <div className="text-xs text-gray-500 font-mono bg-gray-50 p-2 rounded">
                  {compiledModelId}
                </div>
              </div>
            )}
          </div>

          {/* Publishing */}
          <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
            <h3 className="text-lg font-semibold text-gray-900 mb-4">Publish</h3>
            
            <div className="space-y-4">
              <div className="text-sm text-gray-600">
                <p className="mb-2">Publishing requirements:</p>
                <ul className="space-y-1">
                  <li className={`flex items-center ${title.trim() ? 'text-green-600' : 'text-gray-400'}`}>
                    <CheckCircle className="w-4 h-4 mr-2" />
                    Program title
                  </li>
                  <li className={`flex items-center ${description.trim() ? 'text-green-600' : 'text-gray-400'}`}>
                    <CheckCircle className="w-4 h-4 mr-2" />
                    Description
                  </li>
                  <li className={`flex items-center ${author.trim() ? 'text-green-600' : 'text-gray-400'}`}>
                    <CheckCircle className="w-4 h-4 mr-2" />
                    Author name
                  </li>
                  <li className={`flex items-center ${specification.trim() ? 'text-green-600' : 'text-gray-400'}`}>
                    <CheckCircle className="w-4 h-4 mr-2" />
                    Specification
                  </li>
                  <li className={`flex items-center ${compilerModel && interpreterModel ? 'text-green-600' : 'text-gray-400'}`}>
                    <CheckCircle className="w-4 h-4 mr-2" />
                    Model selection
                  </li>
                </ul>
              </div>

              <button
                onClick={handlePublish}
                disabled={publishing || !isFormValid}
                className="w-full px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors flex items-center justify-center"
              >
                {publishing ? (
                  <>
                    <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white mr-2"></div>
                    Publishing...
                  </>
                ) : (
                  <>
                    <Save className="w-4 h-4 mr-2" />
                    Publish Program
                  </>
                )}
              </button>

              {!compiled && (
                <p className="text-xs text-amber-600">
                  Note: You can publish without compiling, but users won't be able to test your program.
                </p>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default PublishProgramPage;
