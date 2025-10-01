import React from 'react';
import { FileText } from 'lucide-react';

interface SpecInputProps {
  value: string;
  onChange: (value: string) => void;
  placeholder?: string;
}

const SpecInput: React.FC<SpecInputProps> = ({
  value,
  onChange,
  placeholder = "Describe what you want your program to do..."
}) => {
  return (
    <div className="card p-6">
      <div className="flex items-center space-x-2 mb-4">
        <FileText className="w-5 h-5 text-primary-600" />
        <h3 className="text-lg font-semibold text-gray-900">Program Specification</h3>
      </div>
      
      <div className="space-y-2">
        <label className="text-sm font-medium text-gray-700">
          Describe your program's functionality
        </label>
        <textarea
          value={value}
          onChange={(e) => onChange(e.target.value)}
          placeholder={placeholder}
          rows={6}
          className="textarea-field"
        />
        <p className="text-xs text-gray-500">
          Be specific about what inputs your program should accept and what outputs it should produce.
        </p>
      </div>
    </div>
  );
};

export default SpecInput;
