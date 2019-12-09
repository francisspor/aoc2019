using System;
using System.Collections.Generic;
using System.Linq;

namespace _04 {
    class Program {
        static void Main (string[] args) {
            int goodPassword = 0;
            int goodPassword2 = 0;

            for (int i = 284639; i <= 748759; i++) {
                List<int> digits = i.ToString ().ToCharArray ().Select (x => Int32.Parse (x.ToString ())).ToList ();

                if (validPassword (digits)) {
                    goodPassword++;

                    if (hasOnlyTwo (digits)) {
                        goodPassword2++;
                    }
                }
            }

            Console.WriteLine ("part1: " + goodPassword);
            Console.WriteLine ("part2: " + goodPassword2);

        }

        private static bool validPassword (List<int> digits, bool part2 = false) {
            var currentValue = digits[0];

            bool hasDouble = false;
            for (int i = 1; i < digits.Count; i++) {
                if (currentValue == digits[i]) {
                    if (hasDouble && part2) {
                        hasDouble = false;
                    } else {
                        hasDouble = true;
                    }
                }

                if (currentValue > digits[i]) {
                    return false;
                }

                currentValue = digits[i];
            }

            Console.WriteLine (string.Join (' ', digits));

            return true && hasDouble;
        }

        private static bool hasOnlyTwo (List<int> digits) {
            var count = 1;
            for (var i = 1; i < digits.Count; i++) {
                if (digits[i] == digits[i - 1]) {
                    count++;
                } else {
                    if (count == 2) {
                        return true;
                    }
                    count = 1;
                }
            }
            return (count == 2);
        }
    }
}