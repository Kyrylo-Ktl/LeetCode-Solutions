public class Solution {

    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public int minNumberOfHours(int initialEnergy, int initialExperience, int[] energy, int[] experience) {
        int hours = 0;

        for (int i = 0; i < energy.length; ++i) {
            // Adding the missing amount of energy
            int extraEnergy = Math.max(0, energy[i] - initialEnergy + 1);
            initialEnergy += extraEnergy;

            // Adding the missing amount of experience
            int extraExperience = Math.max(0, experience[i] - initialExperience + 1);
            initialExperience += extraExperience;

            initialEnergy -= energy[i];
            initialExperience += experience[i];

            hours += extraEnergy + extraExperience;
        }

        return hours;
    }
}
