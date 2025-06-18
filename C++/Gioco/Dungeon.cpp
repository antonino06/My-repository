#include <iostream>

using namespace std;

constexpr auto W = 10;
constexpr auto H = 10;

    char map [W][H];

void init_map()  
{
    for (auto y = 0; y < H; y++) {
        for (auto x = 0; x < W; x++) {
            map[y][x] = '.';
        }
    }
}

void print_entity(int x, int y, char glyph) 
{
    map[x][y] = glyph;
}

int main()
{
    char hero_glyph = '@';
    int hero_x = 5, hero_y = 7;
    cout << "Il nostro eroe " << hero_glyph << " ti saluta!\n";

    // init mappa
    init_map();

    // posiziono eroe sulla mappa
    print_entity(hero_x, hero_y, hero_glyph);

    // stampa mappa
    for (auto y = 0; y < H; y++) {
        for (auto x = 0; x < W; x++) {
            cout << map[y][x];
        }
        cout << endl;
    }
    
    return 0;
}