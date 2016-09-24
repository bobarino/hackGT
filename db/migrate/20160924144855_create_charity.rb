class CreateCharity < ActiveRecord::Migration
  def change
    create_table :charities do |t|
      t.string :name
      t.integer :co_merchant_id
    end
  end
end
