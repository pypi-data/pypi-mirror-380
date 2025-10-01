import React from 'react';
import { ChevronDown } from 'lucide-react';

interface ModelOption {
  id: string;
  name: string;
  description: string;
}

interface ModelSelectorProps {
  label: string;
  options: ModelOption[];
  value: string;
  onChange: (value: string) => void;
  loading?: boolean;
  placeholder?: string;
}

const ModelSelector: React.FC<ModelSelectorProps> = ({
  label,
  options,
  value,
  onChange,
  loading = false,
  placeholder = "Select a model..."
}) => {
  return (
    <div className="flex flex-col space-y-2">
      <label className="text-sm font-medium text-gray-700">{label}</label>
      <div className="relative">
        <select
          value={value}
          onChange={(e) => onChange(e.target.value)}
          disabled={loading}
          className="input-field appearance-none pr-10 cursor-pointer disabled:opacity-50 disabled:cursor-not-allowed"
        >
          <option value="">{loading ? "Loading..." : placeholder}</option>
          {options.map((option) => (
            <option key={option.id} value={option.id}>
              {option.name}
            </option>
          ))}
        </select>
        <ChevronDown className="absolute right-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-gray-400 pointer-events-none" />
      </div>
      {value && (
        <p className="text-xs text-gray-500">
          {options.find(opt => opt.id === value)?.description}
        </p>
      )}
    </div>
  );
};

export default ModelSelector;
