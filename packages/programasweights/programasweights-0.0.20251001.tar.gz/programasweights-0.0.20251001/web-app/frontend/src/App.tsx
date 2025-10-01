import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Toaster } from 'react-hot-toast';
import MainInterface from './components/MainInterface';
import Header from './components/Header';
import AboutPage from './components/AboutPage';
import LeaderboardPage from './components/LeaderboardPage';
import ProgramDetailPage from './components/ProgramDetailPage';
import PublishProgramPage from './components/PublishProgramPage';

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-50">
        <Toaster 
          position="top-right"
          toastOptions={{
            duration: 4000,
            style: {
              background: '#363636',
              color: '#fff',
            },
          }}
        />
        <Header />
        <main className="container mx-auto px-4 py-8">
          <Routes>
            <Route path="/" element={<MainInterface />} />
            <Route path="/about" element={<AboutPage />} />
            <Route path="/leaderboard" element={<LeaderboardPage />} />
            <Route path="/program/:id" element={<ProgramDetailPage />} />
            <Route path="/publish" element={<PublishProgramPage />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;