/*
    Without using queue/stack. (This solution works but is not intuitively appropriate)

    Suppose there is a circle. There are N petrol pumps on that circle. Petrol pumps are numbered 0 to N-1 (both inclusive). 
    You have two pieces of information corresponding to each of the petrol pump: 
    (1) the amount of petrol that particular petrol pump will give, and 
    (2) the distance from that petrol pump to the next petrol pump.

    Initially, you have a tank of infinite capacity carrying no petrol. You can start the tour at any of the petrol pumps. 
    Calculate the first point from where the truck will be able to complete the circle. 
    Consider that the truck will stop at each of the petrol pumps. The truck will move one kilometer for each litre of the petrol.
*/

#include <bits/stdc++.h>

using namespace std;


int truckTour(vector<vector<int>> petrolpumps) {
    int qty = 0, n = petrolpumps.size(), pump_num = 0;
    for (int i = 0; i < n; i++) {
        qty = qty - petrolpumps[i][1] + petrolpumps[i][0];
        if (qty < 0) {
            pump_num = i + 1;
            qty = 0;
        }
    }

    return pump_num;
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;
    vector<vector<int>> petrolPumps;
    for (int i = 0; i < n; i++) {
        int qty, distance;
        cin >> qty >> distance;
        petrolPumps.push_back({qty, distance});
    }

    int result = truckTour(petrolPumps);

    cout << result << "\n";

    return 0;
}