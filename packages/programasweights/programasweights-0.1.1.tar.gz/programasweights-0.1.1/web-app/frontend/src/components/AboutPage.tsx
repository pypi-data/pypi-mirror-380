import { Brain, Code, Zap, Users, BookOpen, Github, ExternalLink } from 'lucide-react';

const AboutPage: React.FC = () => {
  return (
    <div className="max-w-4xl mx-auto">
      {/* Hero Section */}
      <div className="text-center mb-12">
        <div className="flex items-center justify-center w-20 h-20 bg-blue-600 rounded-2xl mx-auto mb-6">
          <Brain className="w-12 h-12 text-white" />
        </div>
        <h1 className="text-4xl font-bold text-gray-900 mb-4">
          ProgramAsWeights
        </h1>
        <p className="text-xl text-gray-600 max-w-2xl mx-auto">
          A revolutionary neural program compiler that transforms natural language specifications 
          into executable neural network weights.
        </p>
      </div>

      {/* What is it Section */}
      <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-8 mb-8">
        <h2 className="text-2xl font-bold text-gray-900 mb-4 flex items-center">
          <BookOpen className="w-6 h-6 mr-3 text-blue-600" />
          What is ProgramAsWeights?
        </h2>
        <div className="prose prose-gray max-w-none">
          <p className="text-gray-700 mb-4">
            ProgramAsWeights represents a paradigm shift in how we think about programming and neural networks. 
            Instead of writing traditional code, you describe what you want your program to do in natural language, 
            and our system compiles it directly into neural network weights that can execute your specification.
          </p>
          <p className="text-gray-700 mb-4">
            This approach bridges the gap between human intent and machine execution, making programming more 
            accessible while leveraging the power of neural computation. The resulting "programs" are not just 
            interpretations of your specifications—they are learned representations that can generalize and 
            adapt to new inputs.
          </p>
        </div>
      </div>

      {/* How it Works */}
      <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-8 mb-8">
        <h2 className="text-2xl font-bold text-gray-900 mb-6 flex items-center">
          <Code className="w-6 h-6 mr-3 text-blue-600" />
          How It Works
        </h2>
        <div className="grid md:grid-cols-3 gap-6">
          <div className="text-center">
            <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center mx-auto mb-3">
              <span className="text-blue-600 font-bold text-lg">1</span>
            </div>
            <h3 className="font-semibold text-gray-900 mb-2">Specify</h3>
            <p className="text-gray-600 text-sm">
              Write a natural language description of what your program should do, 
              along with input-output examples.
            </p>
          </div>
          <div className="text-center">
            <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center mx-auto mb-3">
              <span className="text-blue-600 font-bold text-lg">2</span>
            </div>
            <h3 className="font-semibold text-gray-900 mb-2">Compile</h3>
            <p className="text-gray-600 text-sm">
              Our neural compiler transforms your specification into optimized 
              neural network weights.
            </p>
          </div>
          <div className="text-center">
            <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center mx-auto mb-3">
              <span className="text-blue-600 font-bold text-lg">3</span>
            </div>
            <h3 className="font-semibold text-gray-900 mb-2">Execute</h3>
            <p className="text-gray-600 text-sm">
              Run your compiled neural program on new inputs and get results 
              that generalize beyond your examples.
            </p>
          </div>
        </div>
      </div>

      {/* Key Features */}
      <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-8 mb-8">
        <h2 className="text-2xl font-bold text-gray-900 mb-6 flex items-center">
          <Zap className="w-6 h-6 mr-3 text-blue-600" />
          Key Features
        </h2>
        <div className="grid md:grid-cols-2 gap-6">
          <div>
            <h3 className="font-semibold text-gray-900 mb-2">Natural Language Programming</h3>
            <p className="text-gray-600 text-sm mb-4">
              Write programs using natural language descriptions instead of traditional code.
            </p>
          </div>
          <div>
            <h3 className="font-semibold text-gray-900 mb-2">Neural Compilation</h3>
            <p className="text-gray-600 text-sm mb-4">
              Advanced AI models compile your specifications into executable neural weights.
            </p>
          </div>
          <div>
            <h3 className="font-semibold text-gray-900 mb-2">Generalization</h3>
            <p className="text-gray-600 text-sm mb-4">
              Programs learn from examples and can handle inputs beyond the training data.
            </p>
          </div>
          <div>
            <h3 className="font-semibold text-gray-900 mb-2">Community Sharing</h3>
            <p className="text-gray-600 text-sm mb-4">
              Share your neural programs with the community and discover others' creations.
            </p>
          </div>
        </div>
      </div>

      {/* Use Cases */}
      <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-8 mb-8">
        <h2 className="text-2xl font-bold text-gray-900 mb-6">Use Cases</h2>
        <div className="space-y-4">
          <div className="border-l-4 border-blue-500 pl-4">
            <h3 className="font-semibold text-gray-900">Text Processing</h3>
            <p className="text-gray-600 text-sm">
              Create programs for text classification, sentiment analysis, summarization, and more.
            </p>
          </div>
          <div className="border-l-4 border-green-500 pl-4">
            <h3 className="font-semibold text-gray-900">Data Transformation</h3>
            <p className="text-gray-600 text-sm">
              Build neural programs that transform and process structured data.
            </p>
          </div>
          <div className="border-l-4 border-purple-500 pl-4">
            <h3 className="font-semibold text-gray-900">Pattern Recognition</h3>
            <p className="text-gray-600 text-sm">
              Develop programs that recognize patterns and make predictions from examples.
            </p>
          </div>
          <div className="border-l-4 border-orange-500 pl-4">
            <h3 className="font-semibold text-gray-900">Creative Generation</h3>
            <p className="text-gray-600 text-sm">
              Generate creative content like stories, poems, or structured outputs.
            </p>
          </div>
        </div>
      </div>

      {/* Community */}
      <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-8 mb-8">
        <h2 className="text-2xl font-bold text-gray-900 mb-6 flex items-center">
          <Users className="w-6 h-6 mr-3 text-blue-600" />
          Join the Community
        </h2>
        <p className="text-gray-700 mb-6">
          ProgramAsWeights is more than just a tool—it's a community of researchers, developers, 
          and enthusiasts exploring the future of programming. Share your neural programs, 
          vote on others' creations, and collaborate on pushing the boundaries of what's possible.
        </p>
        <div className="flex flex-wrap gap-4">
          <a
            href="/leaderboard"
            className="inline-flex items-center px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
          >
            <span>Explore Leaderboard</span>
            <ExternalLink className="w-4 h-4 ml-2" />
          </a>
          <a
            href="/publish"
            className="inline-flex items-center px-4 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 transition-colors"
          >
            <span>Publish Your Program</span>
            <ExternalLink className="w-4 h-4 ml-2" />
          </a>
          <a
            href="https://github.com/programasweights"
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center px-4 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 transition-colors"
          >
            <Github className="w-4 h-4 mr-2" />
            <span>GitHub</span>
          </a>
        </div>
      </div>

      {/* Getting Started */}
      <div className="bg-gradient-to-r from-blue-50 to-indigo-50 rounded-xl p-8 border border-blue-200">
        <h2 className="text-2xl font-bold text-gray-900 mb-4">Ready to Get Started?</h2>
        <p className="text-gray-700 mb-6">
          Try compiling your first neural program today. Start with a simple specification 
          and see how ProgramAsWeights transforms your ideas into executable neural networks.
        </p>
        <a
          href="/"
          className="inline-flex items-center px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors font-medium"
        >
          <Code className="w-5 h-5 mr-2" />
          Start Compiling
        </a>
      </div>
    </div>
  );
};

export default AboutPage;
