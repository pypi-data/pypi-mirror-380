import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { 
  ChevronUp, 
  ChevronDown, 
  Trophy, 
  Calendar, 
  User, 
  Tag, 
  ExternalLink,
  Filter,
  Search,
  SortAsc,
  SortDesc
} from 'lucide-react';
import type { Program, ProgramListResponse } from '../types';
import { apiClient } from '../utils/api';
import toast from 'react-hot-toast';

const LeaderboardPage: React.FC = () => {
  const [programs, setPrograms] = useState<Program[]>([]);
  const [loading, setLoading] = useState(true);
  const [sortBy, setSortBy] = useState<'votes' | 'date' | 'title'>('votes');
  const [sortOrder, setSortOrder] = useState<'asc' | 'desc'>('desc');
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedTag, setSelectedTag] = useState<string>('');
  const [page, setPage] = useState(1);
  const [totalCount, setTotalCount] = useState(0);
  const [allTags, setAllTags] = useState<string[]>([]);

  const pageSize = 20;

  useEffect(() => {
    loadPrograms();
  }, [page, sortBy, sortOrder]);

  const loadPrograms = async () => {
    try {
      setLoading(true);
      const response: ProgramListResponse = await apiClient.getPrograms(
        page, 
        pageSize, 
        `${sortBy}_${sortOrder}`
      );
      
      if (response.success) {
        setPrograms(response.programs);
        setTotalCount(response.totalCount);
        
        // Extract unique tags
        const tags = new Set<string>();
        response.programs.forEach(program => {
          program.tags.forEach(tag => tags.add(tag));
        });
        setAllTags(Array.from(tags).sort());
      } else {
        toast.error(response.error || 'Failed to load programs');
      }
    } catch (error) {
      toast.error('Failed to load programs');
      console.error('Error loading programs:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleVote = async (programId: string, voteType: 'up' | 'down') => {
    try {
      const response = await apiClient.voteProgram({ programId, voteType });
      
      if (response.success) {
        // Update the program in the list
        setPrograms(prevPrograms => 
          prevPrograms.map(program => 
            program.id === programId 
              ? { ...program, votes: response.newVoteCount, userVote: response.userVote }
              : program
          )
        );
        toast.success(`Vote ${voteType === 'up' ? 'up' : 'down'} recorded!`);
      } else {
        toast.error(response.error || 'Failed to vote');
      }
    } catch (error) {
      toast.error('Failed to vote');
      console.error('Error voting:', error);
    }
  };

  const filteredPrograms = programs.filter(program => {
    const matchesSearch = searchTerm === '' || 
      program.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
      program.description.toLowerCase().includes(searchTerm.toLowerCase()) ||
      program.author.toLowerCase().includes(searchTerm.toLowerCase());
    
    const matchesTag = selectedTag === '' || program.tags.includes(selectedTag);
    
    return matchesSearch && matchesTag;
  });

  const handleSort = (newSortBy: 'votes' | 'date' | 'title') => {
    if (sortBy === newSortBy) {
      setSortOrder(sortOrder === 'asc' ? 'desc' : 'asc');
    } else {
      setSortBy(newSortBy);
      setSortOrder('desc');
    }
    setPage(1);
  };

  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric'
    });
  };

  const getRankIcon = (index: number) => {
    if (index === 0) return <Trophy className="w-5 h-5 text-yellow-500" />;
    if (index === 1) return <Trophy className="w-5 h-5 text-gray-400" />;
    if (index === 2) return <Trophy className="w-5 h-5 text-amber-600" />;
    return <span className="w-5 h-5 flex items-center justify-center text-gray-500 font-medium">{index + 1}</span>;
  };

  if (loading && programs.length === 0) {
    return (
      <div className="flex items-center justify-center min-h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
      </div>
    );
  }

  return (
    <div className="max-w-6xl mx-auto">
      {/* Header */}
      <div className="text-center mb-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-4 flex items-center justify-center">
          <Trophy className="w-8 h-8 mr-3 text-yellow-500" />
          Neural Programs Leaderboard
        </h1>
        <p className="text-gray-600">
          Discover and vote for the best neural programs created by the community
        </p>
      </div>

      {/* Filters and Search */}
      <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6 mb-6">
        <div className="flex flex-col lg:flex-row gap-4">
          {/* Search */}
          <div className="flex-1">
            <div className="relative">
              <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-5 h-5" />
              <input
                type="text"
                placeholder="Search programs, authors, descriptions..."
                className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
              />
            </div>
          </div>

          {/* Tag Filter */}
          <div className="lg:w-48">
            <div className="relative">
              <Filter className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-5 h-5" />
              <select
                className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent appearance-none bg-white"
                value={selectedTag}
                onChange={(e) => setSelectedTag(e.target.value)}
              >
                <option value="">All Tags</option>
                {allTags.map(tag => (
                  <option key={tag} value={tag}>{tag}</option>
                ))}
              </select>
            </div>
          </div>

          {/* Sort Controls */}
          <div className="flex gap-2">
            <button
              onClick={() => handleSort('votes')}
              className={`px-4 py-2 rounded-lg flex items-center gap-2 ${
                sortBy === 'votes' 
                  ? 'bg-blue-100 text-blue-700 border border-blue-300' 
                  : 'bg-gray-100 text-gray-700 border border-gray-300'
              }`}
            >
              <Trophy className="w-4 h-4" />
              Votes
              {sortBy === 'votes' && (sortOrder === 'asc' ? <SortAsc className="w-4 h-4" /> : <SortDesc className="w-4 h-4" />)}
            </button>
            <button
              onClick={() => handleSort('date')}
              className={`px-4 py-2 rounded-lg flex items-center gap-2 ${
                sortBy === 'date' 
                  ? 'bg-blue-100 text-blue-700 border border-blue-300' 
                  : 'bg-gray-100 text-gray-700 border border-gray-300'
              }`}
            >
              <Calendar className="w-4 h-4" />
              Date
              {sortBy === 'date' && (sortOrder === 'asc' ? <SortAsc className="w-4 h-4" /> : <SortDesc className="w-4 h-4" />)}
            </button>
          </div>
        </div>
      </div>

      {/* Programs List */}
      <div className="space-y-4">
        {filteredPrograms.map((program, index) => (
          <div key={program.id} className="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
            <div className="flex items-start gap-4">
              {/* Rank */}
              <div className="flex flex-col items-center">
                {getRankIcon(index)}
                <div className="text-xs text-gray-500 mt-1">#{index + 1}</div>
              </div>

              {/* Voting */}
              <div className="flex flex-col items-center">
                <button
                  onClick={() => handleVote(program.id, 'up')}
                  className={`p-1 rounded-md transition-colors ${
                    program.userVote === 'up'
                      ? 'text-green-600 bg-green-100'
                      : 'text-gray-400 hover:text-green-600 hover:bg-green-50'
                  }`}
                >
                  <ChevronUp className="w-5 h-5" />
                </button>
                <span className="text-sm font-medium text-gray-900 py-1">
                  {program.votes}
                </span>
                <button
                  onClick={() => handleVote(program.id, 'down')}
                  className={`p-1 rounded-md transition-colors ${
                    program.userVote === 'down'
                      ? 'text-red-600 bg-red-100'
                      : 'text-gray-400 hover:text-red-600 hover:bg-red-50'
                  }`}
                >
                  <ChevronDown className="w-5 h-5" />
                </button>
              </div>

              {/* Program Info */}
              <div className="flex-1">
                <div className="flex items-start justify-between mb-2">
                  <Link 
                    to={`/program/${program.id}`}
                    className="text-xl font-semibold text-gray-900 hover:text-blue-600 flex items-center gap-2"
                  >
                    {program.title}
                    <ExternalLink className="w-4 h-4" />
                  </Link>
                  <div className="flex items-center gap-4 text-sm text-gray-500">
                    <div className="flex items-center gap-1">
                      <User className="w-4 h-4" />
                      {program.author}
                    </div>
                    <div className="flex items-center gap-1">
                      <Calendar className="w-4 h-4" />
                      {formatDate(program.createdAt)}
                    </div>
                  </div>
                </div>

                <p className="text-gray-700 mb-3 line-clamp-2">
                  {program.description}
                </p>

                <div className="flex items-center gap-4 text-sm text-gray-600">
                  <div>
                    <span className="font-medium">Compiler:</span> {program.compilerModel}
                  </div>
                  <div>
                    <span className="font-medium">Interpreter:</span> {program.interpreterModel}
                  </div>
                </div>

                {/* Tags */}
                {program.tags.length > 0 && (
                  <div className="flex items-center gap-2 mt-3">
                    <Tag className="w-4 h-4 text-gray-400" />
                    <div className="flex flex-wrap gap-2">
                      {program.tags.map(tag => (
                        <span
                          key={tag}
                          className="px-2 py-1 bg-gray-100 text-gray-700 rounded-full text-xs cursor-pointer hover:bg-gray-200"
                          onClick={() => setSelectedTag(tag)}
                        >
                          {tag}
                        </span>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            </div>
          </div>
        ))}
      </div>

      {filteredPrograms.length === 0 && !loading && (
        <div className="text-center py-12">
          <Trophy className="w-12 h-12 text-gray-400 mx-auto mb-4" />
          <h3 className="text-lg font-medium text-gray-900 mb-2">No programs found</h3>
          <p className="text-gray-600">
            {searchTerm || selectedTag 
              ? 'Try adjusting your search or filter criteria.'
              : 'Be the first to publish a neural program!'
            }
          </p>
          <Link
            to="/publish"
            className="inline-flex items-center px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors mt-4"
          >
            Publish Program
          </Link>
        </div>
      )}

      {/* Pagination */}
      {totalCount > pageSize && (
        <div className="flex justify-center mt-8">
          <div className="flex items-center gap-2">
            <button
              onClick={() => setPage(Math.max(1, page - 1))}
              disabled={page === 1}
              className="px-3 py-2 border border-gray-300 rounded-lg disabled:opacity-50 disabled:cursor-not-allowed hover:bg-gray-50"
            >
              Previous
            </button>
            <span className="px-4 py-2 text-gray-700">
              Page {page} of {Math.ceil(totalCount / pageSize)}
            </span>
            <button
              onClick={() => setPage(Math.min(Math.ceil(totalCount / pageSize), page + 1))}
              disabled={page >= Math.ceil(totalCount / pageSize)}
              className="px-3 py-2 border border-gray-300 rounded-lg disabled:opacity-50 disabled:cursor-not-allowed hover:bg-gray-50"
            >
              Next
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default LeaderboardPage;
