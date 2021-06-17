/*
    Using queue. (More intuitive)

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


struct petrolPump {
    int petrolQty;
    int distance;
};


int truckTour(queue<petrolPump> petrolpumps) {
    int startpoint = 0, qty = 0, passedpumps = 0;
    while (passedpumps < petrolpumps.size()) {
        petrolPump p = petrolpumps.front();
        qty += p.petrolQty;
        petrolpumps.pop();

        if (qty >= p.distance) {
            passedpumps++;
            qty -= p.distance;
        } else {
            startpoint += passedpumps + 1;
            qty = passedpumps = 0;
        }

        petrolpumps.push(p);
    }

    return startpoint;
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;
    queue<petrolPump> petrolpumps;
    for (int i = 0; i < n; i++) {
        petrolPump p;
        cin >> p.petrolQty >> p.distance;
        petrolpumps.push(p);
    }

    int result = truckTour(petrolpumps);

    cout << result << "\n";

    return 0;
}