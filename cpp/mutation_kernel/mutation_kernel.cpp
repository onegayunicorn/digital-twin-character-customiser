// mutation_kernel: nucleotide sequence analysis kernel (C++17).
//
// Functions:
//   - scan_codons(seq, frame): walk codons from a reading frame, report
//     stop codons (TAG/TGA/TAA) and their codon index / base position.
//   - has_premature_stop(seq, frame, expected_length): true if a stop codon
//     appears before the expected coding length (truncation signal).
//   - gc_content(seq): GC fraction.
//
// Build:   make
// Usage:   ./mutation_kernel scan <sequence> [frame]
//          ./mutation_kernel premature <sequence> <frame> <expected_codons>
//          ./mutation_kernel gc <sequence>
//
// Honest note: analysis kernel only. Outputs sequence facts, never clinical
// claims.
#include <algorithm>
#include <cctype>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>

namespace {

bool IsStopCodon(const std::string& codon) {
  return codon == "TAG" || codon == "TGA" || codon == "TAA";
}

std::string Normalize(const std::string& s) {
  std::string out;
  out.reserve(s.size());
  for (char c : s) {
    char u = static_cast<char>(std::toupper(static_cast<unsigned char>(c)));
    if (u == 'A' || u == 'C' || u == 'G' || u == 'T' || u == 'U') {
      out.push_back(u == 'U' ? 'T' : u);
    }
  }
  return out;
}

struct StopHit {
  int codon_index;   // 0-based codon index within the frame
  int base_position; // 0-based base position
  std::string codon;
};

std::vector<StopHit> ScanCodons(const std::string& seq, int frame) {
  std::vector<StopHit> hits;
  for (int i = frame; i + 2 < static_cast<int>(seq.size()); i += 3) {
    std::string codon = seq.substr(i, 3);
    if (IsStopCodon(codon)) {
      hits.push_back({(i - frame) / 3, i, codon});
    }
  }
  return hits;
}

double GcContent(const std::string& seq) {
  if (seq.empty()) return 0.0;
  size_t gc = 0;
  for (char c : seq) {
    if (c == 'G' || c == 'C') ++gc;
  }
  return static_cast<double>(gc) / static_cast<double>(seq.size());
}

int CmdScan(const std::vector<std::string>& args) {
  if (args.size() < 2) {
    std::cerr << "usage: mutation_kernel scan <sequence> [frame]\n";
    return 1;
  }
  const std::string seq = Normalize(args[1]);
  const int frame = args.size() > 2 ? std::atoi(args[2].c_str()) : 0;
  if (frame < 0 || frame > 2) {
    std::cerr << "frame must be 0..2\n";
    return 1;
  }
  const auto hits = ScanCodons(seq, frame);
  std::cout << "sequence_length=" << seq.size() << " frame=" << frame
            << " stops=" << hits.size() << "\n";
  for (const auto& h : hits) {
    std::cout << "stop codon_index=" << h.codon_index
              << " base=" << h.base_position << " codon=" << h.codon << "\n";
  }
  return 0;
}

int CmdPremature(const std::vector<std::string>& args) {
  if (args.size() < 4) {
    std::cerr << "usage: mutation_kernel premature <seq> <frame> <expected_codons>\n";
    return 1;
  }
  const std::string seq = Normalize(args[1]);
  const int frame = std::atoi(args[2].c_str());
  const int expected = std::atoi(args[3].c_str());
  const auto hits = ScanCodons(seq, frame);
  bool premature = false;
  for (const auto& h : hits) {
    if (h.codon_index < expected) {
      premature = true;
      break;
    }
  }
  std::cout << "premature_stop=" << (premature ? "true" : "false")
            << " first_stop_codon_index="
            << (hits.empty() ? -1 : hits.front().codon_index)
            << " expected_codons=" << expected << "\n";
  return 0;
}

int CmdGc(const std::vector<std::string>& args) {
  if (args.size() < 2) {
    std::cerr << "usage: mutation_kernel gc <sequence>\n";
    return 1;
  }
  const std::string seq = Normalize(args[1]);
  std::cout << "gc_content=" << GcContent(seq) << "\n";
  return 0;
}

}  // namespace

int main(int argc, char** argv) {
  const std::vector<std::string> args(argv + 1, argv + argc);
  if (args.empty()) {
    std::cerr << "usage: mutation_kernel <scan|premature|gc> ...\n";
    return 1;
  }
  const std::string cmd = args[0];
  if (cmd == "scan") return CmdScan(args);
  if (cmd == "premature") return CmdPremature(args);
  if (cmd == "gc") return CmdGc(args);
  std::cerr << "unknown command: " << cmd << "\n";
  return 1;
}
